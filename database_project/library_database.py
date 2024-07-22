import sqlite3


with sqlite3.connect('library.db') as db:
    cursor = db.cursor()
    query = """
    CREATE TABLE IF NOT EXIST Books (
        BookID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        Author VARCHAR(50),
        GenreID INTEGER,
        PublisherID INTEGER,
        Year INTEGER,
        Pages INTEGER,
        Language TEXT,
        Number_of_copies INTEGER
    );
    CREATE TABLE IF NOT EXISTS Readers (
        ReaderID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        Address TEXT,
        PhoneNumber TEXT,
        Email TEXT
        
    );
    CREATE TABLE IF NOT EXISTS Employees (
        EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        Position TEXT,
        PhoneNumber TEXT,
        Email TEXT,
        WorkHours INTEGER
    );
    CREATE TABLE IF NOT EXISTS Categories (
        CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
        CategoryName TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS Genres (
        GenreID INTEGER PRIMARY KEY AUTOINCREMENT,
        GenreName TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS Publishers (
        PublisherID INTEGER PRIMARY KEY AUTOINCREMENT,
        PublisherName TEXT NOT NULL,
        Address TEXT,
        PhoneNumber TEXT,
        Email TEXT
    );
    
    CREATE TABLE IF NOT EXISTS Fines (
        FineID INTEGER PRIMARY KEY AUTOINCREMENT,
        ReaderID INTEGER,
        BookID INTEGER,
        Amount REAL,
        Status TEXT,
        FOREIGN KEY (ReaderID) REFERENCES Readers(ReaderID),
        FOREIGN KEY (BookID) REFERENCES Books(BookID)
    );

    CREATE TABLE IF NOT EXISTS Transactions (
        TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
        BookID INTEGER,
        ReaderID INTEGER,
        TransactionType TEXT,
        TransactionDate TEXT,
        FOREIGN KEY (BookID) REFERENCES Books(BookID),
        FOREIGN KEY (ReaderID) REFERENCES Readers(ReaderID)
    );
    CREATE TABLE IF NOT EXISTS Reviews (
        BookID INTEGER,
        ReaderID INTEGER,
        ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
        Rating INTEGER CHECK(Rating BETWEEN 1 AND 5),
        Comment TEXT,
        ReviewDate TEXT,
        FOREIGN KEY (BookID) REFERENCES Books(BookID),
        FOREIGN KEY (ReaderID) REFERENCES Readers(ReaderID)
    );
        
    """
    cursor.executescript(query)
    cursor.executescript("INSERT INTO Books VALUES()")

    cursor.execute("SELECT * FROM Books")
    print(cursor.fetchall())

