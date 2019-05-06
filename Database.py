import sqlite3

# Objective: Get Data from the converter table in database and fill the List with From and To Column
def populate():
    conn = sqlite3.connect('converter.db')
    cur = conn.cursor()
    value_from = []
    query = cur.execute('SELECT conv_from,conv_to FROM converter')

    for row in query:
        value_from.append(row[0])
        value_from.append(row[1])
    return list(set(value_from))
