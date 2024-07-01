import sqlite3
def connect():
    con=sqlite3.connect("food.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS meoww (id INTEGER PRIMARY KEY,food text , material text ,meow text)")
    con.commit()
    con.close()

def insert(food,material,meow):
    con=sqlite3.connect("food.db")
    cur = con.cursor()
    cur.execute("INSERT INTO meoww VALUES (NUll ,?,?,?)",(food,material,meow))
    con.commit()
    con.close()
def view():
    con=sqlite3.connect("food.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM meoww")
    rows = cur.fetchall()
    con.close()
    return rows
def f(id):
    con=sqlite3.connect("food.db")
    cur = con.cursor()
    cur.execute("SELECT material FROM meoww WHERE   id=? ",(id,))
    rows = cur.fetchall()
    con.close()
    return rows
def h(food):
    con=sqlite3.connect("food.db")
    cur = con.cursor()
    cur.execute("SELECT material FROM meoww WHERE   food=? ",(food,))
    rows = cur.fetchall()
    con.close()
    return rows
def search(material):
    con=sqlite3.connect("food.db")
    cur = con.cursor()
    cur.execute("SELECT food FROM meoww WHERE   material=?  ",(material,))
    rows = cur.fetchall()
    con.close()
    return rows
def delete(id,):
    con=sqlite3.connect("food.db")
    cur = con.cursor()
    cur.execute("DELETE FROM meoww WHERE id=?",(id,))
    con.commit()
    con.close()
def update():
    con = con=sqlite3.connect("food.db")
    cur = con.cursor()
    cur.execute("SELECT material FROM meoww")
    rows=cur.fetchall()
    con.close()
    return rows

connect()
