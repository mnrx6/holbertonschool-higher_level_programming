#!/usr/bin/python3
"""List states matching the user input."""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 5:
        print("Usage: {} username password db_name state_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    state_name = args[4]
    db_conn = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=data,
        port=3306)

    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}' "
                   "ORDER BY id ASC;".format(state_name))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db_conn.close()
