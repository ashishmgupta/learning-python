import sqlite3
import sys
def login(username, password):
    query = "select * from user where username = '" + username + "' and password = '" + password +"'"
    print(query)
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    rows = cur.execute(query)
    for row in rows:
        print(row)
    

username = sys.argv[1]
password = sys.argv[2]


login(username, password)

# Good input
# python .\sql-injection.py "admin" "admin"
# returns only one record

# Bad input - SQL injection 
# python .\sql-injection.py "admin' OR 1=1 --" "some immaterial password"
# Returns ALL records

# Secure coding practices
##################################
# Input validation
# Use an ORM
# Use paramerized queries/stored procedure instead of inline queries
# Make sure the the account being used for SQL connection is not a privileged account (e.g. SA in SQL server)