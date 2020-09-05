def execute_query(query):
    import sqlite3
    conn = sqlite3.connect('./chinook.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result
