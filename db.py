import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
)
mCursor = conn.cursor()
mCursor.execute("CREATE DATABASE IF NOT EXISTS school_db")
mCursor.execute("CREATE TABLE IF NOT EXISTS school_db.STUDENT( `STUDENT_NO` INT(3) NOT NULL , `STUDENT_NAME` TEXT NOT NULL , `STUDENT_DOB` DATE NOT NULL , `STUDENT_DOJ` DATE NOT NULL )")