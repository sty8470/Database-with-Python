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
@app.route('/index')
def index():
    return '''
<html>
    <head>
        <title>My New Skillz</title>
    </head>
    <body>
        <h1>Woohoo!</h1>
        This is the landing page...
    </body>
</html>'''


@app.route('/movie/<kevin>')
def movies(kevin):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='xodud8470',
                           db='MovieDB',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('SELECT * FROM Movie WHERE title=%s;', [kevin])
    result_lst = []
    if c.rowcount > 0:
        rs = c.fetchall()
        result_lst = [r for r in rs]
        return flask.render_template('movie.html', title=kevin, data=[r for r in rs])
    else:
        return flask.render_template('nomovie.html', title=kevin)



@app.route('/json/movie/<title>')
@support_jsonp
def json_movies(title):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='xodud8470',
                           db='MovieDB',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('SELECT * FROM Movie WHERE title LIKE %s;', [title])
    result_list = []
    if c.rowcount > 0:
        rs = c.fetchall()
        result_list = [r for r in rs]
    s = json.dumps({'movies': result_list})
    return s




# Add a route for star names that allows
# URLs that contain a star's last name and lists
# all stars with that last name.





# Add a route to retrieve a JSON version
# of the star names by last name as described above.








if __name__ == '__main__':
    app.run()
