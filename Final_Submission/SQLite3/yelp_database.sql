CREATE TABLE Business(
    
business_id TEXT PRIMARY KEY,
    
business_name TEXT,
    
neighborhood TEXT,
    
address TEXT,
    
city TEXT,
    
state TEXT,
    
postal_code TEXT,
    
latitude TEXT,
    
longitude TEXT,
    
stars REAL,
    
review_count INTEGER,
    
is_open BOOLEAN,
    
monday TEXT,
    
tuesday TEXT,
    
wednesday TEXT,
    
thursday TEXT,
    
friday TEXT,
    
FOREIGN KEY (business_id) REFERENCES BusinessCategory(business_id) ON DELETE RESTRICT,
    
FOREIGN KEY (business_id) REFERENCES Review(business_id) ON DELETE RESTRICT

);




CREATE TABLE Category(
    
category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    
category_name TEXT UNIQUE NOT NULL,
    
FOREIGN KEY (category_id) REFERENCES BusinessCategory(category_id) ON DELETE RESTRICT

);



CREATE TABLE BusinessCategory(
    
business_id TEXT,
    
category_id INTEGER,
    
PRIMARY KEY (business_id, category_id)

);




CREATE TABLE Review(
    
review_id TEXT PRIMARY KEY,
    
business_id TEXT NOT NULL,
    
user_id TEXT NOT NULL,
    
review_stars REAL,
    
review_date DATE NOT NULL,
    
review_text TEXT,
    
review_useful INTEGER,
    
review_funny INTEGER,
    
review_cool INTEGER,
    
UNIQUE(business_id, user_id, review_date)

);



CREATE TABLE User(
    
user_id TEXT PRIMARY KEY,
    
name TEXT,
    
review_count INTEGER,
    
yelping_since DATE,
    
user_useful INTEGER,
    
user_funny INTEGER,
    
user_cool INTEGER,
    
fans INTEGER,
    
average_stars REAL,
    
FOREIGN KEY (user_id) REFERENCES UserFriend(user_id) ON DELETE RESTRICT,
    
FOREIGN KEY (user_id) REFERENCES UserFriend(friend_id) ON DELETE RESTRICT

);




CREATE TABLE UserFriend(
    
user_id TEXT,
    
friend_id TEXT,
    
PRIMARY KEY (user_id, friend_id)
);
