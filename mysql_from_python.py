import os
import pymysql

# Get Username from workspace
username = os.getenv('C9_USER')

# Connect ti the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    """ close the connection to SQL regardless of whether
     the above was successful or not
    """
    connection.close()
