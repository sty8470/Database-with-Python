import json
import MySQLdb
import MySQLdb.cursors
import flask
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
        <h1>Here are Yelp Popular Restaurant Categories, and their Reviews</h1>
        Choose the zipcode where you live
        <hr>
        <br>
        Choose your favorite restaurant that you usually go to
        <hr>
        <br>
        Select your favorite category of restaurant near your town
    </body>
</html>'''


@app.route('/yelp/<business_name>')
def yelp(business_name):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='xodud8470',
                           db='yelpdb',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('SELECT * FROM business_name WHERE title=%s;', [business_name])
    result_lst = []
    if c.rowcount > 0:
        rs = c.fetchall()
        result_lst = [r for r in rs]
        return flask.render_template('yelp.html', title=business_name, data=[r for r in rs])
    else:
        return flask.render_template('noyelp.html', title=business_name)



@app.route('/yelp/restaurants/<average_stars>')
@support_jsonp
def yelp_average_stars(average_stars):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='xodud8470',
                           db='yelpdb',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('SELECT * FROM average_stars WHERE title LIKE %s;', [average_stars])
    result_list = []
    if c.rowcount > 0:
        rs = c.fetchall()
        result_list = [r for r in rs]
    s = json.dumps({'average_stars': result_list})
    return s

def yelp_text(text):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='xodud8470',
                           db='yelpDB',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('SELECT * FROM text WHERE title LIKE %s;', [text])
    result_list = []
    if c.rowcount > 0:
        rs = c.fetchall()
        result_list = [r for r in rs]
    s = json.dumps({'text': result_list})
    return s




# Add a route for star names that allows
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
