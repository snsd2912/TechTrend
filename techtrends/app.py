import sqlite3
import logging
from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort

db_connection_count = 0

# Set up logging
# Set up logging with a custom format
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('app')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s:app:%(asctime)s, %(message)s', datefmt='%d/%m/%Y, %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.propagate = False

# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    global db_connection_count
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    db_connection_count += 1 
    return connection

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    connection.close()
    return post

def get_post_count():
    connection = get_db_connection()
    cursor = connection.execute('SELECT COUNT(*) FROM posts')
    post_count = cursor.fetchone()[0]
    connection.close()
    return post_count

# Define the Flask application
app = Flask(__name__)

# Define the main route of the web application 
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
      logger.info("Article not found!")
      return render_template('404.html'), 404
    else:
      logger.info(f"Article \"{post['title']}\" retrieved!")
      return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
    logger.info('The "About Us" page is retrieved.')
    return render_template('about.html')

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
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
            logger.info(f"Article \"{title}\" added!")
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/healthz', methods=['GET'])
def healthz():
    return jsonify(result="OK - healthy"), 200

@app.route('/metrics', methods=['GET'])
def metrics():
    post_count = get_post_count()
    metrics_data = {
            "db_connection_count": db_connection_count,
            "post_count": post_count
    }
    return jsonify(metrics_data), 200

# start the application on port 3111
if __name__ == "__main__":
   app.run(host='0.0.0.0', port='3111')
