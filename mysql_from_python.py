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
        list_of_names = ["Fred", "Fred"]
        # Prepare a string with the sanme number of placeholders
        # as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});"
                       .format(format_strings), list_of_names)
    connection.commit()
finally:
    connection.close()
