import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute(" CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text,author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute(" INSERT INTO book values (Null,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search (title="", author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM booK WHERE id=?",(id,))
    conn.commit()
    conn.close()

def  update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()

#insert("sghj","jkeajk",2001,400)
#insert("Jsfn","aryah",2002,300)
#insert("tjhn","atgr",2003,200)
#insert("Joihn","adf",2004,100)
#update(1,"Joihn","joji",2001,900)
#delete(1)
#print(search(author="joji"))
#print(view())

#print(search(author="joji"))
