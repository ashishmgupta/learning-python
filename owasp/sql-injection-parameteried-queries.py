import sqlite3
import sys
def login(username, password):
    query = "select * from user where username = ? and password = ?"
    params = [username, password]
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    rows = cur.execute(query,params)
    for row in rows:
        print(row)
    

username = sys.argv[1]
password = sys.argv[2]


login(username, password)

# Good Input
# python ./sql-injection-parameterized-queries.py "admin2" "admin2"
# retuens the record 

# Bad input
# python ./sql-injection-parameterized-query.py "admin2' OR 1=1 --" "admin"
# returns nothing
