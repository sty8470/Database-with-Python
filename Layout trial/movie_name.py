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



import reading_data



#1. What is the oldest release year?
def question_01(reader):
    min_year = None
    for row in reader:
        if min_year is None or min_year>int(row['movie_year']):
            min_year = int(row['movie_year'])
    return min_year
    #return min([int(row['movie_year']) for row in reader])



#2. How old is the oldest actor?
def question_02(reader):
    return max([int(row['star_age']) for row in reader])



#3. What is the title and date of the oldest horror movie?
def question_03(reader):
    min_year = None
    min_title = None
    for row in reader:
        movie_year = int(row['movie_year'])
        movie_genre = row['movie_genre']
        if min_year is None or (min_year> movie_year and 'Horror' in movie_genre):
            min_year = int(row['movie_year'])
            min_title = row['movie_title']
    return min_year, min_title
    #return min([int(r['movie_year']) for r in reader if 'Horror' in r['movie_genre']])



#4. What producer has the least net worth and what is that net worth?
def question_04(reader):
    min_networth = None
    for row in reader:
        if min_networth is None or min_networth> float(row['producer_net_worth']):
            min_networth = float(row['producer_net_worth'])
            producer_name = row['producer_name']

    return producer_name, min_networth

    '''
      min_worth = None
      min_producer = None
      for row in reader:
          mw = float(row['producer_net_worth'])
          mp = row['producer_name']
          if min_worth is None or (min_worth > mw):
              min_worth = mw
              min_producer = mp
      return min_worth, min_producer
      '''
    

  
#5. Which studio has produced the most movies?
def question_05(reader):
    dict = {}
    lst = []
    for row in reader:
        studio = row['studio_name']
        lst.append(studio)

    #return min(set(lst), key = lst.count)


    for name in lst:
        if name not in dict:
            dict[name] = 1

        else:
            dict[name] += 1

    return dict

#6. How many movies were released in 1977?
def question_06(reader):
    count = 0
    for row in reader:
        if row['movie_year'] == '1977':
            count+=1
    return count

    #return sum([1 if row['movie_year'] == 1977 else 0 for row in reader])


#7. How many movies did Gloria Hastings star in?
def question_07(reader):
    return sum([1 for row in reader if row['star_name'] == 'Gloria Haastings'])

def question_08(reader):
    pass

def question_09(reader):
    lst = []
    for row in reader:
        if ('Comedy' and 'Horror')  in row['movie_genre']:
            lst.append(row['movie_genre'])

    return len(set(lst))

def question_10(reader):
    lst = []
    for row in reader:
        if row['movie_title'] == 'Robin Hood':
            lst.append(row['star_name'])
    return set(lst)

# 11. What stars have been in more than one movie?

def question_11(reader):
    dict = {}
    for row in reader:
        movie_star = row['star_name']
        dict[movie_star] = dict.get(movie_star,0) + 1

    return dict
        
# 12. What movies starred actors who were younger than 6?

def question_12(reader):
    lst = []
    for row in reader:
        age = row['star_age']
        if age < '6':
            lst.append(row['star_name'])
    return lst

# 13. Which actors have worked with the producer with the greatest net worth?

def question_13(reader):
    lst = []
    max_net_worth = 0
    for row in reader:
        net_worth = row['producer_net_worth'] 
        if int(net_worth) > max_net_worth:
            max_net_worth = net_worth
            max_producer = row['producer_name']

    return max_producer, max_net_worth


            
            

def main():
    reader = reading_data.ReusableReader('movie_data.csv')
    for row in reader:
        print(row)
        '''
    q01 = question_01(reader)
    print(q01)
    q04 = question_04(reader)
    print(q04)
    q06 = question_06(reader)
    print("Question of 6 is", q06)
    q07 = question_07(reader)
    print("The answer of question 7 is", q07)
'''        
  

main()
