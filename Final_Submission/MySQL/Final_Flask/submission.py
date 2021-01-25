import json
import MySQLdb
import MySQLdb.cursors
import flask
from flask import Flask, Markup, render_template
app = flask.Flask(__name__, static_folder='static', static_url_path='')



from functools import wraps
from flask import request, current_app


def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f(*args,**kwargs)) + ')'
            return current_app.response_class(content, mimetype='application/javascript')
        else:
            return f(*args, **kwargs)
    return decorated_function

	
	
	
@app.route('/')
#@app.route('/index')
def index():
    return '''
<html>
    <head>
        <title>Yelp Data</title>
    </head>
    <body>

        <form action = "index.php" method = "post">
	<input type = "text" name = "search" placeholder = "Search for restaurant data.."
	<input type = "submit" value = ">>" />
	</form>

        <h1>Here is the Yelp Interface where you can explore the details of Yelp restaurants </h1>

        <p style= "color:hotpink; font-size: 20px;">
        Option 1: Name of restaurant business will show up followed by this rule:  <br>
        Type the name of business inside "<business>" placeholder <br>
        /yelp/business/<business>
        ex) Red Bowl, Toast Cafe, Bubbly Nails

        <hr>
        <br>

        <p style = "color:orange; font-size: 20px;">
        Option 2: Type any rating scale of the restaurant category that you expect out of 5: <br>
        /yelp/review<ratings>
        ex) Bubbly Nails, Cvs Pharmacy

        <hr>
        <br>

        <p style = "color:blue; font-size: 20px;">
        Option 3: Type 
        Select your favorite category of restaurant near where you live: <br>
        /yelp/category/<category>
        
    </body>
</html>'''


@app.route('/yelp/business/<business>')
def yelp_business(business):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='xodud8470',
                           db='yelpdb',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('SELECT * FROM business WHERE business_name=%s;', [business])
    result_lst = []
    if c.rowcount > 0:
        rs = c.fetchall()
        result_lst = [r for r in rs]
        return flask.render_template('yelp_business.html', business_name = business, data=[r for r in rs])
    else:
        return flask.render_template('noyelp_business.html', business_name = business)


@app.route('/yelp/address/<business>')
def yelp_address(business):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='xodud8470',
                           db='yelpdb',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('SELECT * FROM business WHERE business_name=%s;', [business])
    result_lst = []
    if c.rowcount > 0:
        rs = c.fetchall()
        result_lst = [r for r in rs]
        return flask.render_template('yelp_address.html', business_name = business, data=[r for r in rs])
    else:
        return flask.render_template('noyelp_address.html', business_name = business)


@app.route('/yelp/review/<business_name>')
def yelp_review_stars(business_name):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='xodud8470',
                           db='yelpdb',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('SELECT review_stars, business_name FROM Business JOIN Review ON Review.business_id = Business.business_id WHERE business_name = %s', [business_name])
    result_lst = []
    if c.rowcount > 0:
        rs = c.fetchall()
        result_lst = [r for r in rs]
        return flask.render_template('yelp_review.html', categories = business_name, data=[r for r in rs])
    else:
        return flask.render_template('noyelp_review.html', categories = business_name)





@app.route('/yelp/review_text/<category>')
def yelp_categorie(category):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='xodud8470',
                           db='yelpdb',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    s = '''SELECT review_text FROM Category INNER JOIN businesscategory
           ON category.category_id = businessCategory.category_id
           INNER JOIN review 
           ON businesscategory.business_id = review.business_id
           WHERE category.category_name = "Nail Salons";'''
    c.execute(s)#, [category])
    print(s)
    result_lst = []
    if c.rowcount > 0:
        rs = c.fetchall()
        result_lst = [r for r in rs]
        print(result_lst)
        return flask.render_template('yelp_category.html', category_name = category, data=[r for r in rs])
    else:
        return flask.render_template('noyelp_category.html', category_name = category)

@app.route('/json/yelp/restaurants/<business_name>')
@support_jsonp
def yelp_average_stars(business_name):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='xodud8470',
                           db='yelpdb',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('SELECT * FROM Business WHERE business_name LIKE %s;', [business_name])
    result_list = []
    if c.rowcount > 0:
        rs = c.fetchall()
        result_list = [r for r in rs]
    s = json.dumps({'Business': result_list})
    return s

@app.route('/XML/restaurants/<business_name>')
@support_jsonp
def yelp_XML(business_name):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='xodud8470',
                           db='yelpdb',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('SELECT * FROM Business WHERE business_name = %s;', [business_name])
    result_list = []
    if c.rowcount > 0:
        rs = c.fetchall()
        result_list = [r for r in rs]
    x = '<?xml version="1.0" encoding = "UTF-8" ?>\n<businesses>\n'
    for row in result_list:
        x += '<business>'
        x += '<business_id>{}</business_id>;<business_name>{}</business_name>;<address>{} </address>;<latitude> {} </latitutde>;<longitude>{}</longitude>;<review_count>{} </review_count>;'.format(row['business_id'], row['business_name'], row['address'], row['latitude'], row['longitude'], row['review_count'])
        x += '</business>'
    x += '</businesses>'
    return x




labels = [
   'Toast Cafe', 'Bubbly Nails',
   'Red Bowl', 'Dolce Lusso',
   'Nail Palace', 'Jumpin Java',
   'CVS Pharmacy', 'Papa Johns Pizza',
   'Motel6', 'Fort Mill BBQ Company',
   'Casa Columbia'
]

values = [
    6,17, 77, 24, 6, 12, 6, 10, 9, 56, 46
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA",]

@app.route('/bar')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Restaurants in Yelp and their Business_Reviews', max=80, labels=bar_labels, values=bar_values)




# URLs that contain a star's last name and lists
# all stars with that last name.

#@app.route('/star/<lastname>'):
 #   def startname(lastname):
  #      return 'The last name is {}'.format(lastname)
    '''
    conn = MySQLdb.connect(host = 'localhost',
                           user = 'root',
                           passwd ='xodud8470',
                           db = 'MovieDB',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('SELECT * FROM Movie WHERE title =%s;', [title])
    if c.rowcount > 0:
        rs = c.fetchall()
        return flask.render_template('movie.html', title = title, data = [r for r in rs])
    else:
        return flask.render_template('nomovie.html', title = title)
    '''
    
    




# Add a route to retrieve a JSON version
# of the star names by last name as described above.








if __name__ == '__main__':
    app.run()
