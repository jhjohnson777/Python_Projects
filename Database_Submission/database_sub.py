#
# Python Version: 3.10.5
#
# Author: Jack Johnson
#
# Purpose:  The Tech Academy - Python Course, Creating a program that will
#           create a database, adds new data to that database and then
#           queries that database.


# Given list of files
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', \
            'World.txt', 'data.pdf', 'myPhoto.jpg')


import sqlite3

conn = sqlite3.connect('test2.db') # Connects to, or creates, a database

with conn: # with our connection
    cur = conn.cursor() # creates cursor object used to execute sql commands
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file \
        )") # creates a table named tbl_files with a primary key and a file column
    conn.commit() # commits changes to the table in the db
conn.close() # closes connection

conn = sqlite3.connect('test2.db') # Connects to, or creates, a database

for file in fileList: # for loop to iterate through fileList
    if file.endswith(".txt"): # if true, perform the following
        with conn: # with our db connection
            cur = conn.cursor() # cursor object 
            cur.execute("INSERT INTO tbl_files(col_file) VALUES (?)", (file,))
            conn.commit() # inserts file from fileList as a single tuple and commits change to the db
            print(file) # print file name to the console
        


