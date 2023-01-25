import sqlite3
import os

database = "cat_images.db"

# Reset the table if it already exists 
if os.path.isfile(database):
    os.remove(database)
    print("Table successfully reset!")

# Connects with the database
conn = sqlite3.connect(database)
cursor = conn.cursor()

# Creates the table
cursor.execute('''CREATE TABLE cat_images
                (id INTEGER PRIMARY KEY,
                path TEXT,
                name TEXT,
                posted INTEGER DEFAULT 0)''')

#Insert the images in the table
folder = "cats"

def insert_images(folder):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isdir(path):
            insert_images(path)
        elif path.endswith('.jpg'):
            cursor.execute("INSERT INTO cat_images (path, name) VALUES (?, ?)", (path, file))

insert_images(folder)

# Save the changes and close the connection
conn.commit()
conn.close()
