import sqlite3
import time
from tryinit import lst_of_links
from flask import Flask, request, render_template, g, redirect

app = Flask(__name__)
DATABASE = 'cheeps.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def db_read_cheeps():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM cheeps")
    return cur.fetchall()

def db_add_cheep(gifs):
    cur = get_db().cursor()
    t = str(time.time())
    cheep_info = (gifs, gifs, gifs)
    cur.execute("INSERT INTO cheeps VALUES (?, ?, ?)", cheep_info)
    get_db().commit()    

def reddit_links(word, n=5):
	return lst_of_links(word, n)

from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    cheeps = db_read_cheeps()
    print(cheeps)
    return render_template('index2.html', cheeps = cheeps, gifs = [])

@app.route("/api/cheep", methods=["POST"])
def receive_cheep():
    print(request.form)
    #db_add_cheep(request.form['gif'])
    return render_template('index2.html', cheeps = [], gifs = reddit_links(request.form['gif'], 10))

if __name__ == "__main__":
    app.run(debug = True)