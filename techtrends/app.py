import sqlite3
import logging

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort

# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

#====start query get title===========
# Function to get a post using its ID
def get_post(post_id):   
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',(post_id,)).fetchone()
    connection.close()
    return post
#====end query get title===========

#====start query get metric===========
# Function to get count connection
def get_count_connectionne():   
    connection = get_db_connection()
    gce = connection.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
    gcene = gce.fetchone()[0]
    connection.close()
    return gcene

# Function to get count article 
def get_count_article():   
    connection = get_db_connection()
    gca = connection.execute("SELECT COUNT(*) FROM posts")
    gcane = gca.fetchone()[0]
    connection.close()
    return gcane
#====end query get metric===========

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Define the main route
#arl_project_4
@app.route('/', methods=['POST', 'GET'])

def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    #arl_project_3 stream logs to a file
    app.logger.info('The main page is retrieved')
    
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    
    if post is None:    
      #arl_project_3 stream logs to a file
      app.logger.info('The page is not exist!!')
      return render_template('404.html'), 404
    else:     
      #arl_project_3 stream logs to a file
      app.logger.info('The article '+ post['title'] +' is retrieved!!')
    
      return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
    #arl_project_3 stream logs to a file
    app.logger.info('The About Us page is retrieved')
    
    return render_template('about.html')

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    #arl_project_3 stream logs to a file
    app.logger.info('The new post page is retrieved')
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()
            
            #arl_project_3 stream logs to a file
            app.logger.info('The new article '+ title +' is created')

            return redirect(url_for('index'))

    return render_template('create.html')
    
#===============================================================
#arl_project_1 : Define /healthz response
@app.route('/healthz')
def status():
    response = app.response_class(
             response=json.dumps({"result":"OK - healthy"}),
             status=200,
             mimetype='application/json'
    )
    #arl_project_3 stream logs to a file
    app.logger.info('Status request /healthz successfull')
    app.logger.debug('DEBUG message')
    return response
#===============================================================

#===============================================================
#arl_project_2 : Define /metrics response
@app.route('/metrics')
def metrics():
    # execute the queries to get the required metrics
    gacene = get_count_article()
    gecene = get_count_connectionne()
    
    # create the JSON response
    response = {'db_connection_count': gecene, 'post_count': gacene}
    
    #arl_project_3 stream logs to a file
    app.logger.info('Status request /metrics successfull')
    app.logger.debug('DEBUG message')
    
    # return the JSON response with a 200 status code
    return jsonify(response),200
#===============================================================


# start the application on port 3111
if __name__ == "__main__":
   #arl_project_3 stream logs to a file
   #app.run(debug=True)
   #logging.basicConfig(filename='app.log',level=logging.DEBUG) 
   
   app.run(host='0.0.0.0', port='3111', debug=True) 
