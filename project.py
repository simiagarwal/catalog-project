from flask import Flask, render_template, request, redirect,jsonify, url_for, flash

from flask import session as login_session
import random, string
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
app = Flask(__name__)


CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "catalog"

print"project.py file is running"
#Connect to Database and create database session
engine = create_engine('sqlite:///catalogwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/login')
def showLogin():
  state = ' '.join(random.choice(string.ascii_uppercase +string.digits)for x in xrange(32))
  login_session['state'] = state
  return render_template('login.html', STATE=state)




@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = getUserId (login_session['email'])
    if not user_id:
      user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output
#User helper functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


#JSON APIs to view catalog Information
@app.route('/catalog/<int:category_id>/menu/JSON')
def shoeCatalogJSON(catalog_id):
    category= session.query(Category).filter_by(id = category_id).one()
    items = session.query(Item).filter_by(category_id = category_id).all()
    return jsonify(Items=[i.serialize for i in items])


@app.route('/catalog/<int:category_id>/items/<int:item_id>/JSON')
def ItemJSON(category_id, item_id):
    Menu_Item = session.query(Item).filter_by(id = item_id).one()
    return jsonify(Menu_Item = Menu_Item.serialize)

@app.route('/catalog/JSON')
def catalogJSON():
    category = session.query(Category).all()
    return jsonify(category= [r.serialize for r in category])


#Show the catalog
@app.route('/')
@app.route('/catalog/')
def showCatalog():
  print 'hi'
  categories = session.query(Category).order_by(asc(Category.name))
  if 'username' not in login_session:
    return render_template('publiccatalog.html', categories = categories)
  else:
    return render_template("catalog.html",categories = categories)

#Create a new category
@app.route('/catalog/new/', methods=['GET','POST'])
def newCategory():
  if'username' not in login_session:
    return redirect('/login')

  if request.method == 'POST':
      new_Category = Category(name = request.form['name'],user_id = login_session['user_id'])
      session.add(new_Category)
      flash('New Category %s Successfully Created' % newRestaurant.name)
      session.commit()
      return redirect(url_for('showCatelog'))
  else:
      return render_template('newcategory.html')

#Edit a category
@app.route('/catalog/<int:category_id>/edit/', methods = ['GET', 'POST'])
def editCategory(category_id):
  edited_category = session.query(Category).filter_by(id = category_id).one()
  if request.method == 'POST':
      if request.form['name']:
        edited_category.name = request.form['name']
        flash('Category Successfully Edited %s' % edited_category.name)
        return redirect(url_for('showCatelog'))
  else:
    return render_template('newcategory.html', category = edited_category)


#Delete a category
@app.route('/catalog/<int:category_id>/delete/', methods = ['GET','POST'])
def deleteCategory(category_id):
  categoryToDelete = session.query(Category).filter_by(id = category_id).one()
  if 'username' not in login_session:
    return redirect("/login")
  if categoryToDelete.user_id != login_session['user_id']:
    return "<script> function myFunction() {alert('You are not authorized to delete this category.Please create your category in order to delete.');}<script><body onload = myFunction()''>"
  if request.method == 'POST':
    session.delete(categoryToDelete)
    flash('%s Successfully Deleted' % categoryToDelete.name)
    session.commit()
    return redirect(url_for('showCatalog', category_id = category_id))
  else:
    return render_template('deletecategory.html',category = categoryToDelete)

#Show category items
@app.route('/catalog/<int:category_id>/')
@app.route('/catalog/<int:category_id>/menu/')
def showItem(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    items = session.query(Item).filter_by(category_id = category_id).all()
    creator = getUserInfo(catalog.user_id)
    if 'username' not in login_session or creator.id != login_session['user_id']:
      return render_template('publiccatalog.html',items=items,category=category,creator=creator)
    else:
      return render_template('items.html', items = items, category = category,creator=creator)
     


#Create a new  item
@app.route('/catalog/<int:category_id>/item/new/',methods=['GET','POST'])
def newItem(category_id):
  if'username' not in login_session:
    return redirect('/login')

  
  if request.method == 'POST':
      newItem = Item(name = request.form['name'], description = request.form['description'], price = request.form['price'],  category_id = category_id,
        user_id=login_session['user_id'])
      session.add(newItem)
      session.commit()
      flash('New Item %s  Successfully Created' % (newItem.name))
      return redirect(url_for('showCatalog', category_id = category_id))
  else:
      return render_template('newitem.html', category_id = category_id)

#Edit an item
@app.route('/catalog/<int:category_id>/item/<int:item_id>/edit', methods=['GET','POST'])
def editItem(category_id, item_id):

    editedItem = session.query(Item).filter_by(id = item_id).one()
    category = session.query(Category).filter_by(id = category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        
        session.add(editedItem)
        session.commit() 
        flash('%s Item Successfully Edited' %(editedItem.name))
        return redirect(url_for('showCatalog', category_id = category_id))
    else:
        return render_template('edititem.html', category_id = category_id, item_id = item_id, item = editedItem)


#Delete an item
@app.route('/catalog/<int:category_id>/item/<int:item_id>/delete', methods = ['GET','POST'])
def deleteItem(category_id,item_id):
    category = session.query(Category).filter_by(id = category_id).one()
    itemToDelete = session.query(Item).filter_by(id = item_id).one() 
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('%s Item Successfully Deleted'%(itemToDelete.name))
        return redirect(url_for('showCatalog', category_id = category_id))
    else:
        return render_template('deleteitem.html', item = itemToDelete)

@app.route("/about")
def aboutus():
  return render_template("aboutus.html")

@app.route('/partners')
def partners():
  return render_template("partners.html")

@app.route("/contactus")
def contactus():
  return render_template("contactus.html")



if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 8000)
