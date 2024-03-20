# Import required libraries
import sqlite3

# Connect to SQLite database
# New file created if it doesn't already exist
conn = sqlite3.connect('sqlite3.db')

# Create cursor object
cursor = conn.cursor()

# Create and populate tables
cursor.executescript(''' 
CREATE TABLE Advisor( 
AdvisorID INTEGER PRIMARY KEY, 
AdvisorName TEXT NOT NULL 
); 

CREATE TABLE Student( 
StudentID INTEGER PRIMARY KEY, 
StudentName TEXT NOT NULL 
); 

CREATE TABLE Student_Advisor( 
StudentID INTEGER, 
AdvisorID INTEGER, 
FOREIGN KEY(StudentID) REFERENCES Student(StudentID), 
FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID), 
PRIMARY KEY(StudentID, AdvisorID)
); 

INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES 
(1,"nika kurdadze"), 
(2,"saba sabashvili"), 
(3,"nika nikoladze"), 
(4,"goga gogashvili"), 
(5,"giorgi giorgadze"); 

INSERT INTO Student(StudentID, StudentName) VALUES 
(501,"Geek1"), 
(502,"Geek2"), 
(503,"Geek3"), 
(504,"Geek4"), 
(505,"Geek5"), 
(506,"Geek6"), 
(507,"Geek7"), 
(508,"Geek8"), 
(509,"Geek9"), 
(510,"Geek10"); 

INSERT INTO Student_Advisor(StudentID, AdvisorID) VALUES 
(501, 1), 
(502, 1), 
(503, 3), 
(504, 2), 
(505, 4), 
(506, 2), 
(507, 2), 
(508, 3), 
(509, NULL), 
(510, 1); 

''')

conn.commit()

cursor.execute('''
    SELECT Advisor.AdvisorName, COUNT(Student_Advisor.StudentID) AS StudentCount
    FROM Advisor
    LEFT JOIN Student_Advisor ON Advisor.AdvisorID = Student_Advisor.AdvisorID
    GROUP BY Advisor.AdvisorName;
''')

advisors = cursor.fetchall()

for advisor in advisors:
    print(f"Advisor: {advisor[0]}, Students: {advisor[1]}")

conn.close()
