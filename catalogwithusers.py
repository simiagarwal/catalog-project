from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Category, Base, Item, User
 
engine = create_engine('sqlite:///catalogwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

user1 = User(username='Simi Agarwal', email='1simiagarwal@gmail.com')
session.add(user1)
session.commit()

#basketball items 
category1 = Category(name = "Basketball", user = user1)

session.add(category1)
session.commit()




Item1 = Item(
	name = "Ball1",
	sub_category = "equipment",
	description = "UNDER ARMOUR 495 INDOOR/OUTDOOR BALL - MEN'S",
	price = "$40.00",
	category_id= category1.id,
	user = user1,
	
	
)

session.add(Item1)
session.commit()

Item2 = Item(
	name = "ball2",
	sub_category= "equipment", 
 	description = "NIKE VERSA TACK BASKETBALL - MEN'S", 
	price = "$89.99",
	category_id= category1.id,
	user= user1,
	)
	

session.add(Item2)
session.commit()

Item3 = Item(
	name ="bag1",
	sub_category = "accessory", 
	description = "NIKE HOOPS ELITE MAX AIR 2.0 BACKPACK", 
	price = "$183.99",
	category_id= category1.id, 
	user= user1,
	
	)

session.add(Item3)
session.commit()

Item4 = Item(
	name="bag2",
	sub_category = "accessory",
	description = "JORDAN RETRO 13 BACKPACK",
	price = "$150.00",
	category_id = category1.id,
	user = user1,
	
	)

session.add(Item4)
session.commit()

Item5 = Item(
	name ="shoes1",
	sub_category = "clothing",
	description = "Unique cushioning features for all-day wear.", 
	price = "$61.99",
	category_id = category1.id,
	user= user1,
	
	)

session.add(Item5)
session.commit()

Item6 = Item(
	name = "shoes2",
	sub_category = "clothing",
 	description = "NIKE KOBE A.D. - MEN'S", 
 	price = "$96.99",
 	category_id = category1.id,
 	user = user1,
 	
 	)

session.add(Item6)
session.commit()

Item7 = Item(
    name ="shirt1",
	sub_category = "clothing", 
	description = "comfortable cotton shirt", 
	price = "$29.00",
	category_id = category1.id,
	user = user1,
	
	)

session.add(Item7)
session.commit()






# soccer Items
category2 = Category( name ='soccer', user = user1)

session.add(category2)
session.commit()


Item1 = Item(
	name = "ball1",
	sub_category = "equipment", 
	description = "NIKE STRIKE SOCCER BALL.", 
	price = "$47.99",
	category_id = category2.id,
	user= user1
	
	)

session.add(Item1)
session.commit()

Item2 = Item(
	name ="shirt1",
	sub_category = "clothing",
	description = " delivers a soft feel, sweat-wicking performance",
	price = "$25",
	category_id = category2.id,
	user= user1,
	
	)

session.add(Item2)
session.commit()

Item3 = Item(
	name="pants1",
	sub_category = "clothing", 
	description = "Cotton", 
	price = "$59.99",
	category_id = category2.id,
	user= user1,
	)

session.add(Item3)
session.commit()

Item4 = Item(
	name="pants2",
	sub_category = "clothing ", 
	description = "Mixed", 
	price = "$40.00",
	category_id = category2.id,
	user = user1,
	
	)

session.add(Item4)
session.commit()

Item5 = Item(
	name = "shoes1",
	sub_category = "clothing", 
	description = "ADIDAS NEMEZIZ TANGO 17.1 TRAINER - MEN'S", 
	price = "$150.00",
	category_id = category2.id,
	user= user1,
	
	)

session.add(Item5)
session.commit()

Item6 = Item(
	name ="shoes2",
	sub_category = "clothing", 
	description = "ADIDAS NEMEZIZ TANGO 17.1 TRAINER - MEN'S",
	price = "$99.00",
	category_id = category2.id,
	user= user1,
	
	)

session.add(Item6)
session.commit()




# baseball items
category3 = Category(name = "baseball",user=user1)

session.add(category3)
session.commit()


Item1 = Item(
	name = "Bat1",
	sub_category = "equipment", 
	description = "Louisville Slugger Junior Big Barrel Omaha 517 2 3/4 (-10) Baseball Bat", 
	price = "$69.99",
	category_id = category3.id,
	user= user1,
	
	
	)

session.add(Item1)
session.commit()

Item2 = Item(
	name = "Bat2",
	sub_category="equipment", 
	description = "FLASHTEK Natural Baseball Bat",
	price = "18.99",
	category_id = category3.id,
	user= user1,
	
	)

session.add(Item2)
session.commit()

Item3 = Item(
	name="shoes1",
	sub_category = "clothing", 
	description = "Under Armour Men's Leadoff Low RM Baseball Cleats", 
	price = "$89.99", 
	category_id = category3.id,
	user= user1,
	

	)

session.add(Item3)
session.commit()

Item4 = Item(
	name = "bag1",
	sub_category = "accessory", 
	description = "Athletico Baseball Bat Bag - Backpack for Baseball, T-Ball & Softball Equipment & Gear for Kids, Youth, and Adults | Holds Bat, Helmet, Glove, & Shoes | Separate Shoe Compartment, & Fence Hook",
	price = "$59.99",
	category_id = category3.id,
	user = user1,
	
	)

session.add(Item4)
session.commit()
###########
user2 = User(username='simi', email='simiagarwal@yahoo.com')
session.add(user1)
session.commit()

#snowboarding
category4 = Category(name = "snowboarding", user = user2)

session.add(category4)
session.commit()




Item1 = Item(
	name = "board1",
	sub_category = "equipment",
	description = "Revolution 101 Balance Board Trainer.",
	price = "$100.00",
	category_id= category4.id,
	user = user2,
	
	
)

session.add(Item1)
session.commit()

Item2 = Item(
	name = "board2",
	sub_category = "equipment", 
 	description = "HangTime Snowboard Wall Mount", 
	price = "$19.99",
	category_id= category4.id,
	user = user2,
	)
	

session.add(Item2)
session.commit()

Item3 = Item(
	name ="bag1",
	sub_category = "accessory", 
	description = "Dry Bag Waterproof Floating Dry Gear Bags for Boating, Kayaking, Fishing, Rafting, Swimming, Camping and Snowboarding-Camouflage ", 
	price = "$183.99",
	category_id= category4.id, 
	user= user2,
	
	)

session.add(Item3)
session.commit()

Item4 = Item(
	name="bag2",
	sub_category = "accessory",
	description = "SARKI 30L Waterproof Backpack-Dry Bag with Zipper Pocket and Padded Shoulder Straps - Large Dry Sack for Kayaking,Beach,Snowboarding,Water Sports,Boating - with Waterproof Pouch",
	price="$99.00",
	category_id= category4.id,
	user = user2,
	
	)

session.add(Item4)
session.commit()

Item5 = Item(
	name ="shoes1",
	sub_category= "clothing",
	description = "Firefly Snowboard Snowboarding Shoes C30 Gladiator", 
	price = "$161.99",
	category_id= category4.id,
	user = user2,
	
	)

session.add(Item5)
session.commit()

Item6 = Item(
	name = "shoes2",
	sub_category = "clothing",
 	description = "Yaktrax Walk Traction Cleats for Walking on Snow and Ice", 
 	price = "$15.99",
 	category_id= category4.id,
 	user = user2,
 	
 	)

session.add(Item6)
session.commit()

Item7 = Item(
    name ="gloves1",
	sub_category = "accessory", 
	description = "Ski Gloves,RunRRIn Winter Warmest Waterproof and Breathable Snow Gloves for Mens,Womens,ladies and Kids Skiing,Snowboarding", 
	price = "$19.00",
	category_id= category4.id,
	user= user2,
	
	)

session.add(Item7)
session.commit()

Item8 = Item(
	name = "gogles1",
	sub_category = "accessory", 
	description = "OutdoorMaster Ski Goggles PRO - Frameless, Interchangeable Lens 100% UV400 Protection Snow Goggles for Men & Women - with Portable Storage Box",
 	price="$59.99",
 	category_id= category4.id,
 	user = user2,
 	
 	)

session.add(Item8)
session.commit()




# #Men Items
# category2 = Category( category_type ='men', user = user2)

# session.add(category2)
# session.commit()


# Item1 = Item(
# 	name = "shirt1",
# 	item_type = "Shirts", 
# 	description = "T-shirt for modern-day cool.", 
# 	price = "$147.99",
# 	category_id = category2.id,
# 	user_id = user2.id,
# 	category_type ='men'
# 	)

# session.add(Item1)
# session.commit()

# Item2 = Item(
# 	name ="shirt2",
# 	item_type = "Shirts",
# 	description = " delivers a soft feel, sweat-wicking performance",
# 	price = "$125",
# 	category_id = category2.id,
# 	user_id = user2.id,
# 	category_type ='men'
# 	)

# session.add(Item2)
# session.commit()

# Item3 = Item(
# 	name="pants1",
# 	item_type = "Pants", 
# 	description = "Cotton", 
# 	price = "$159.99",
# 	category_id = category2.id,
# 	user_id = user2.id,
# 	category_type ='men')

# session.add(Item3)
# session.commit()

# Item4 = Item(
# 	name="pants2",
# 	item_type = "Pants ", 
# 	description = "Mixed", 
# 	price = "$140.00",
# 	category_id = category2.id,
# 	user_id = user2.id,
# 	category_type ='men'
# 	)

# session.add(Item4)
# session.commit()

# Item5 = Item(
# 	name = "shoes1",
# 	item_type = "Shoes", 
# 	description = "Luxary leather", 
# 	price = "$150.00",
# 	category_id = category2.id,
# 	user_id = user2.id,
# 	category_type ='men'
# 	)

# session.add(Item5)
# session.commit()

# Item6 = Item(
# 	name ="shoes2",
# 	item_type = "Shoes", 
# 	description = "Enjoy the open seas and warm breeze in fine style thanks to these comfortable boat shoes",
# 	price = "$160.00",
# 	category_id = category2.id,
# 	user_id = user2.id,
# 	category_type ='men'
# 	)

# session.add(Item6)
# session.commit()




# # #Home items
# # category3 = Category(category_type = "home",user=user2)

# # session.add(category3)
# # session.commit()


# Item1 = Item(
# 	name = "appliance1",
# 	item_type = "Appliances", 
# 	description = "Employing a unique tilting head to facilitate bowl and content removal, this mixer is undeniably handy. 1-year hassle-free replacement warranty.", 
# 	price = "$249.99",
# 	category_id = category3.id,
# 	user_id = user2.id,
# 	category_type = "home"
	
# 	)

# session.add(Item1)
# session.commit()

# Item2 = Item(
# 	name = "towels1",
# 	item_type = "Towels", 
# 	description = "Ultra-soft and extra-absorbent, these towels make a blissful addition to your bath. In favorite neutrals, gentle pastels and rich jewel tones, the standout selection of shades can accommodate every de,cor.", 
# 	price = "10.99",
# 	category_id = category3.id,
# 	user_id = user2.id,
# 	category_type = "home"
# 	)

# session.add(Item2)
# session.commit()

# Item3 = Item(
# 	name="sheets1",
# 	item_type = "Sheets", 
# 	description = "Tcozy 300-thread-count Pima cotton grounds with a rich buttery tone and contrast floral accents.", 
# 	price = "$29.99", 
# 	category_id = category3.id,
# 	user_id = user2.id,
# 	category_type = "home"
# 	)

# session.add(Item3)
# session.commit()

# Item4 = Item(
# 	name = "furniture1",
# 	item_type = "Furniture", 
# 	description = "Traditional Queen Anne styling with with the added feature of reclining comfort. Plush cushioning sits on elegant cabriole legs and features a classic rolled-arm silhouette. The perfect addition to a common area.", 
# 	price = "$799.99",
# 	category_id = category3.id,
# 	user_id = user2.id,
# 	category_type = "home"
# 	)

# session.add(Item4)
# session.commit()



''' # #Menu for Thyme for that
# category1 = category(item_type = "Thyme for That Vegetarian Cuisine ", user=user1)

# session.add(category1)
# session.commit()


# Item1 = Item(item_type = "Tres Leches Cake", description = "Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.", price = "", category_type = "", category = category1)

# session.add(Item1)
# session.commit()

# Item2 = Item(item_type = "Mushroom risotto", description = "Portabello mushrooms in a creamy risotto", price = "", category_type = "", category = category1)

# session.add(Item2)
# session.commit()

# Item3 = Item(item_type = "Honey Boba Shaved Snow", description = "Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", price = "", category_type = "", category = category1)

# session.add(Item3)
# session.commit()

# Item4 = Item(item_type = "Cauliflower Manchurian", description = "Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions", price = "", category_type = "", category = category1)

# session.add(Item4)
# session.commit()

# Item5 = Item(item_type = "Aloo Gobi Burrito", description = "Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom", price = "", category_type = "", category = category1)

# session.add(Item5)
# session.commit()




#Menu for Tony's Bistro
# category1 = category(item_type = "Tony\'s Bistro ")

# session.add(category1)
# session.commit()


# Item1 = Item(item_type = "Shellfish Tower", description = "", price = "", category_type = "", category = category1)

# session.add(Item1)
# session.commit()

# Item2 = Item(item_type = "Chicken and Rice", description = "", price = "", category_type = "", category = category1)

# session.add(Item2)
# session.commit()

# Item3 = Item(item_type = "Mom's Spaghetti", description = "", price = "", category_type = "", category = category1)

# session.add(Item3)
# session.commit()

# Item4 = Item(item_type = "Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)", description = "", price = "", category_type = "", category = category1)

# session.add(Item4)
# session.commit()

# Item5 = Item(item_type = "Tonkatsu Ramen", description = "Noodles in a delicious pork-based broth with a soft-boiled egg", price = "", category_type = "", category = category1)

# session.add(Item5)
# session.commit()




# #Menu for Andala's 
# category1 = category(item_type = "Andala\'s")

# session.add(category1)
# session.commit()


# Item1 = Item(item_type = "Lamb Curry", description = "Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.", price = "", category_type = "", category = category1)

# session.add(Item1)
# session.commit()

# Item2 = Item(item_type = "Chicken Marsala", description = "Chicken cooked in Marsala wine sauce with mushrooms", price = "", category_type = "", category = category1)

# session.add(Item2)
# session.commit()

# Item3 = Item(item_type = "Potstickers", description = "Delicious chicken and veggies encapsulated in fried dough.", price = "", category_type = "", category = category1)

# session.add(Item3)
# session.commit()

# Item4 = Item(item_type = "Nigiri SamplerMaguro, Sake, Hamachi, Unagi, Uni, TORO!", description = "", price = "", category_type = "", category = category1)

# session.add(Item4)
# session.commit()




# #Menu for Auntie Ann's
# category1 = category(item_type = "Auntie Ann\'s Diner ")

# session.add(category1)
# session.commit()

# Item9 = Item(item_type = "Chicken Fried Steak", description = "Fresh battered sirloin steak fried and smothered with cream gravy", price = "$8.99", category_type = "Entree", category = category1)

# session.add(Item9)
# session.commit()



# Item1 = Item(item_type = "Boysenberry Sorbet", description = "An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness", price = "", category_type = "", category = category1)

# session.add(Item1)
# session.commit()

# Item2 = Item(item_type = "Broiled salmon", description = "Salmon fillet marinated with fresh herbs and broiled hot & fast", price = "", category_type = "", category = category1)

# session.add(Item2)
# session.commit()

# Item3 = Item(item_type = "Morels on toast (seasonal)", description = "Wild morel mushrooms fried in butter, served on herbed toast slices", price = "", category_type = "", category = category1)

# session.add(Item3)
# session.commit()

# Item4 = Item(item_type = "Tandoori Chicken", description = "Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.", price = "", category_type = "", category = category1)

# session.add(Item4)
# session.commit()




# #Menu for Cocina Y Amor
# category1 = category(item_type = "Cocina Y Amor ")

# session.add(category1)
# session.commit()


# Item1 = Item(item_type = "Super Burrito Al Pastor", description = "Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", price = "", category_type = "", category = category1)

# session.add(Item1)
# session.commit()

# Item2 = Item(item_type = "Cachapa", description = "Golden brown, corn-based venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ", price = "", category_type = "", category = category1)

# session.add(Item2)
# session.commit()

print "added items!"

 '''