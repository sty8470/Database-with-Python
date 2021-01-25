import sqlite3
import csv

csv_file = open('yelp_csv.csv')
reader = csv.DictReader(csv_file)

conn = sqlite3.connect('yelp_data.db')
c = conn.cursor()

for row in reader:

    business_query = 'INSERT INTO Business VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

    try:
        c.execute(business_query, (
            row["business_id"], row["business_name"].replace("'", "''"), row["neighborhood"].replace("'", "''"),
            row["address"].replace("'", "''"), row["city"].replace("'", "''"), row["state"], row["postal_code"],
            row["latitude"], row["longitude"], row["business_stars"], row["business_review_count"], row["is_open"],
            row["monday"], row["tuesday"], row["wednesday"], row["thursday"], row["friday"]))
    except sqlite3.IntegrityError as ex:
        pass

    category_list = row["categories"].split(";")
    for category in category_list:
        try:
            c.execute("INSERT INTO Category (category_name) VALUES (?)", (category.replace("'", "''"),))
        except sqlite3.IntegrityError as ex:
            pass
        try:
            c.execute(
                "INSERT INTO BusinessCategory (business_id, category_id) VALUES (?, (SELECT category_id FROM Category WHERE category_name = ?))",
                (row['business_id'], category.replace("'", "''")))
        except sqlite3.IntegrityError as ex:
            pass

    review_query = 'INSERT INTO Review VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'

    c.execute(review_query, (row['review_id'], row['business_id'], row['user_id'], row['review_stars'], row['date'],
                             row['text'].replace("'", "''"), row['review_useful'], row['review_funny'],
                             row['review_cool']))

    user_query = 'INSERT INTO User VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'

    try:
        c.execute(user_query, (row['user_id'],
                               row['user_name'].replace("'", "''"), row['user_review_count'], row['yelping_since'],
                               row['user_useful'], row['user_funny'], row['user_cool'],
                               row['fans'], row['average_stars']))
    except sqlite3.IntegrityError as ex:
        pass

    friends_list = row['friends'].split(';')
    try:
        for friend_id in friends_list:
            c.execute('INSERT INTO UserFriend VALUES (?, ?)', (row['user_id'], friend_id))
    except sqlite3.IntegrityError as ex:
        pass

all_rows = c.fetchall()
for row in all_rows:
    print(row)

conn.commit()
conn.close()
