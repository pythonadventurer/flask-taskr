from views import db
from _config import DATABASE_PATH

import sqlite3
from datetime import datetime

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    # temporarily change name of the tasks table
    c.execute ("""ALTER TABLE tasks RENAME TO old_tasks""")

    # recreate a new tasks table with updates schema
    db.create_all()

    # retrieve data from old_tasks tabke
    c.execute("""SELECT name, due_date, priority, status
                 FROM old_tasks ORDER_BY task_id ASC""")

    # save all rows as a list of tuples; set posted_date to now and user_id to 1
    data = [(row[0], row[1], row[2], row[3],
            datetime.now(), 1) for row in c.fetchall()]

    # insert data into tasks table
    c.executemany("""INSERT INTO tasks (name, due_date, priority, status,
                       posted_date, user_id) VALUES(?, ?, ?, ?, ?, ?)""", data)

    # delete old tasks table
    c.execute("DROP TABLE old_tasks")

