#!/usr/bin/python3
"""List all cities with their state names."""

import MySQLdb
import sys

if __name__ == "__main__":
    db_conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db_conn.cursor()
    cursor.execute('''
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC''')

    cities = cursor.fetchall()

    for city in cities:
        print(citie)

    cursor.close()
    db_conn.close()
