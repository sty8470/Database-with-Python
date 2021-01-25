import csv


#   Questions
# =============
#  1. What is the oldest release year?
#  2. How old is the oldest actor?
#  3. What is the title and date of the oldest horror movie?
#  4. What producer has the least net worth and what is that net worth?
#  5. Which studio has produced the most movies?
#  6. How many movies were released in 1977?
#  7. How many movies did Gloria Hastings star in?
#  8. How many comedy movies are there?
#  9. Which movies are both comedies and horror films?
# 10. Who starred in "Robin Hood"?
# 11. What stars have been in more than one movie?
# 12. What movies starred actors who were younger than 6?
# 13. Which actors have worked with the producer with the greatest net worth?

class ReusableReader:
    def __init__(self, filename):
        self.__data = []
        self.__keys = []
        with open(filename) as mfile:
            csvreader = csv.DictReader(mfile)
            self.__data = list(csvreader)
            self.__keys = csvreader.fieldnames

    def __iter__(self):
        return iter(self.__data)


def question_01(reader):
    '''
    min_year = None
    for row in reader:
        if min_year is None or min_year > int(row['movie_year']):
            min_year = int(row['movie_year'])
    return min_year
    '''
    return min([int(r['movie_year']) for r in reader])


def question_02(reader):
    return max([int(r['star_age']) for r in reader])


def question_03(reader):
    min_year = None
    min_title = None
    for row in reader:
        my = int(row['movie_year'])
        mg = row['movie_genre']
        if min_year is None or (min_year > my and 'Horror' in mg):
            min_year = my
            min_title = row['movie_title']
    return min_year, min_title
    
    #return min([(int(r['movie_year']), r['movie_title']) \
    #            for r in reader if 'Horror' in r['movie_genre']], key=lambda x: x[0])


def question_06(reader):
    pass


def question_10(reader):
    pass



def main():
    reader = ReusableReader('movie_data.csv')
    for row in reader:
        print(row)
        '''
    q01 = question_01(reader)
    print(q01)
    q02 = question_02(reader)
    print(q02)
    q03 = question_03(reader)
    print(q03)
    '''
    



if __name__ == '__main__':
    main()
