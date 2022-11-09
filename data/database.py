import sqlite3

database = sqlite3.connect('database.db')
cursor = database.cursor()
create_table = '''CREATE TABLE IF NOT EXISTS "main"."users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "created_at" TEXT NOT NULL,
    "updated_at" TEXT NOT NULL
);'''

database.execute(create_table)

