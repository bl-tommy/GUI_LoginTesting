import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "aburns4309", hashlib.sha256("FemB0ys!".encode()).hexdigest()
username2, password2 = "csherrick1906", hashlib.sha256("Rumcoke1!".encode()).hexdigest()
username3, password3 = "admin", hashlib.sha256("Secur3Pa55w0rd!".encode()).hexdigest()
username4, password4 = "ttesterson2305", hashlib.sha256("TestTesterson".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username4, password4))

conn.commit()


