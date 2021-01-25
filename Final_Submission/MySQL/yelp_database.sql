CREATE TABLE Business(
    
business_id VARCHAR(255) PRIMARY KEY,
    
business_name VARCHAR(255),
    
neighborhood VARCHAR(255),
    
address VARCHAR(255),
    
city VARCHAR(255),
    
state VARCHAR(255),
    
postal_code VARCHAR(255),
    
latitude VARCHAR(255),
    
longitude VARCHAR(255),
    
stars REAL,
    
review_count INT,
    
is_open BOOL,
    
monday VARCHAR(255),
    
tuesday VARCHAR(255),
    
wednesday VARCHAR(255),
    
thursday VARCHAR(255),
    
friday VARCHAR(255)    
);


CREATE TABLE Category(
    
category_id INT PRIMARY KEY AUTO_INCREMENT,
    
category_name VARCHAR(255) UNIQUE NOT NULL    
);



CREATE TABLE BusinessCategory(
    
business_id VARCHAR(255),
    
category_id INT,
    
PRIMARY KEY (business_id, category_id),

FOREIGN KEY (business_id) REFERENCES Business(business_id) ON DELETE RESTRICT,
  
FOREIGN KEY (category_id) REFERENCES Category(category_id) ON DELETE RESTRICT
  
);



CREATE TABLE Review(
    
review_id VARCHAR(255) PRIMARY KEY,
    
business_id VARCHAR(255) NOT NULL,
    
user_id VARCHAR(255) NOT NULL,
    
review_stars REAL,
    
review_date DATE NOT NULL,
    
review_text VARCHAR(5000),
    
review_useful INT,
    
review_funny INT,
    
review_cool INT,
    
UNIQUE(business_id, user_id, review_date)
,
FOREIGN KEY (business_id) REFERENCES Business(business_id) ON DELETE RESTRICT

);



CREATE TABLE UserFriend(
    
user_id VARCHAR(255),
    
friend_id VARCHAR(255),
    
PRIMARY KEY (user_id, friend_id)
);


CREATE TABLE User(
    
user_id VARCHAR(255) PRIMARY KEY,
    
name VARCHAR(255),
    
review_count INT,
    
yelping_since DATE,
    
user_useful INT,
    
user_funny INT,
    
user_cool INT,
    
fans INT,
    
average_stars REAL,
    
FOREIGN KEY (user_id) REFERENCES UserFriend(user_id) ON DELETE RESTRICT
);



