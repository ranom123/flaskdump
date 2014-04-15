from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
app = Flask(__name__, static_url_path = "", static_folder = "static")

@app.before_request
def before_request():
   g.db = sqlite3.connect("names.db")

@app.teardown_request
def teardown_request(exception):
   if hasattr(g, 'db'):
      g.db.close()

@app.route('/')
def index():
   author = 'KEK'
   name = 'visitor'
   return render_template('index.html', author=author, name=name)

@app.route('/continue', methods = ['GET', 'POST'])
def continue_():
   getname = request.form['name']
   g.db.execute("INSERT INTO nametable VALUES (?)", [getname])
   g.db.commit()
   print("We found a visitor! Name: "+getname)
   return redirect('/')

@app.route('/culprits')
def culprits():
   nametable = g.db.execute("SELECT name FROM nametable").fetchall()
   return render_template('culprits.html', nametable = nametable)

if __name__ == "__main__":
   app.run()
   

