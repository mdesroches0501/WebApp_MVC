# models.py - handles everything that involves a Database
import sqlite

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('toDo.db')
        self.createUserTable()
        self.createToDoTable()
    
    def createToDoTable(self)

        query = ""
        CREATE TABLE IF NOT EXISTS "ToDo" (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Description TEXT,
            _is_done boolean,
            _is_deleted boolean,
            CreatedOn Date DEFAULT CURRENT_DATE,
            DueDate Date,
            UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        ""

        self.conn.execute(query)

    def createUserTable(self)

        query = ""
        CREATE TABLE IF NOT EXISTS "User" (
            id INTEGER PRIMARY KEY,
            Name TEXT,
            Email TEXT
        );
        ""

        self.conn.execute(query)

