import os
import datetime
import pymysql

# Get Username from workspace
username = os.getenv('C9_USER')

# Connect ti the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')
"""
try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # close the connection to SQL regardless of whether
    # the above was successful or not

    connection.close()



try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    connection.close()
"""

try:
    with connection.cursor() as cursor:
        row = ("Bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
finally:
    connection.close()
