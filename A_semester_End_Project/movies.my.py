import csv
import os
import MySQLdb




def main():
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='xodud8470',
                           db='MovieDB')
    c = conn.cursor()

    studio_insert = 'INSERT INTO Studio (name) VALUES (%s);'
    producer_insert = 'INSERT INTO Producer (name, net_worth) VALUES (%s, %s);'
    movie_insert = 'INSERT INTO Movie (title, year, length, studio_id, producer_id) VALUES (%s, %s, %s, %s, %s);'
    star_insert = 'INSERT INTO Star (name, birth_year) VALUES (%s, %s);'
    genre_insert = 'INSERT INTO Genre (name) VALUES (%s);'
    movie_genre_insert = 'INSERT INTO MovieGenre (movie_id, genre_id) VALUES (%s, %s);'
    movie_star_insert = 'INSERT INTO MovieStar (movie_id, star_id) VALUES (%s, %s);'
    with open('movie_data.csv', encoding='utf8') as mfile:
        csvreader = csv.DictReader(mfile)
        for row in csvreader:
            
            try:
                c.execute(studio_insert, [row['studio_name']])
                studio_id = c.lastrowid
            except MySQLdb.IntegrityError:
                c.execute('SELECT studio_id FROM Studio WHERE name=%s;', [row['studio_name']])
                studio_id = c.fetchone()[0]

            try:
                c.execute(producer_insert, [row['producer_name'], row['producer_net_worth']])
                producer_id = c.lastrowid
            except MySQLdb.IntegrityError:
                c.execute('SELECT producer_id FROM Producer WHERE name=%s;', [row['producer_name']])
                producer_id = c.fetchone()[0]
            
            try:
                c.execute(movie_insert, [row['movie_title'], row['movie_year'], row['movie_length'], studio_id, producer_id])
                movie_id = c.lastrowid
            except MySQLdb.IntegrityError:
                c.execute('SELECT movie_id FROM Movie WHERE title=%s AND year=%s;', [row['movie_title'], row['movie_year']])
                movie_id = c.fetchone()[0]
            
            star_year = 2018 - int(row['star_age'])
            try:
                c.execute(star_insert, [row['star_name'], star_year])
                star_id = c.lastrowid
            except MySQLdb.IntegrityError:
                c.execute('SELECT star_id FROM Star WHERE name=%s AND birth_year=%s;', [row['star_name'], star_year])
                star_id = c.fetchone()[0]
            
            genres = row['movie_genre'].split('|')
            for genre in genres:
                try:
                    c.execute(genre_insert, [genre])
                    genre_id = c.lastrowid
                except MySQLdb.IntegrityError:
                    c.execute('SELECT genre_id FROM Genre WHERE name=%s;', [genre])
                    genre_id = c.fetchone()[0]
                try:
                    c.execute(movie_genre_insert, [movie_id, genre_id])
                except MySQLdb.IntegrityError:
                    pass

            try:
                c.execute(movie_star_insert, [movie_id, star_id])
            except MySQLdb.IntegrityError:
                pass

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
