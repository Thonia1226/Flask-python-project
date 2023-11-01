#The flask python with all the libraries

rom flask import Flask, render_template, request,session
import sqlite3 as sql
app = Flask(__name__)

#conn = sql.connect('database.db')
#print("Opened database successfully")

#conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
#print("Table created successfully")

# conn.close()

@app.route('/')
def home():
    name="Student management system"
    return render_template('home.html',name = name)

@app.route('/enternew')
def new_student():
   return render_template('student.html')

@app.route('/login',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         pin = request.form['pin']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin))
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()
