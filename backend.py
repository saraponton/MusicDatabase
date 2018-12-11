import sqlite3


class Backend(object):
    def __init__(self):
        db = sqlite3.connect("music.db")
        cur= db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS music(id INTEGER PRIMARY KEY, title TEXT, singer TEXT, year INT)")
        db.commit()
        db.close()

    def add(self, title="", singer="", year= ""):
        db = sqlite3.connect("music.db")
        cur = db.cursor()
        cur.execute("INSERT INTO music VALUES (NULL, ?, ? , ?)", (title, singer, year))
        db.commit()
        db.close()


    def view_all(self):
        db = sqlite3.connect("music.db")
        cur = db.cursor()
        cur.execute("SELECT * FROM music")
        rows = cur.fetchall()
        db.close()
        return rows

    def delete(self,id):
        db = sqlite3.connect("music.db")
        cur = db.cursor()
        cur.execute("DELETE FROM music WHERE id =?" , (id,))
        db.commit()
        db.close()



