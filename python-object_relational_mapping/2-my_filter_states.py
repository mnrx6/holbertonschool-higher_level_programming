#!/usr/bin/python3
"""List states matching the user input."""

import MySQLdb
import sys

if __name__ == "__main__":
    db_conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        state_name=sys.argv[4]
    )

    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}' "
                   "ORDER BY id ASC;".format(state_name))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db_conn.close()
