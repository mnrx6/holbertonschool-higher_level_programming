#!/usr/bin/python3
"""List all cities of a given state."""

import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 5:
        print("Usage: {} username password db_name state_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    db_conn = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=data,
        port=3306
    )
    cur = db_conn.cursor()
    execute_cur = cur.execute('''
        SELECT cities.name
        FROM cities INNER JOIN states
        ON cities.state_id=states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        ''', (args[4],))

    cities = cur.fetchall()
    names = [city[0] for city in cities]
    print(", ".join(names))

    cur.close()
    db_conn.close()
