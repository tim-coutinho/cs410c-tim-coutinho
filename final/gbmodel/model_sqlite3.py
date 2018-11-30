"""
Data is stored in a SQLite database with the columns title, author,
ingredients, time, skill, description, and tooltip.
"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'entries.db'  # Local file for our database


class model(Model):
    def __init__(self):
        super().__init__()  # Set defaults
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute('SELECT COUNT(title) FROM recipes')
        except sqlite3.OperationalError:
            cursor.execute('''
                CREATE TABLE recipes
                (title TEXT, author TEXT, ingredients TEXT, time INTEGER, skill INTEGER, description TEXT, tooltip TEXT)''')
            for recipe in self.defaults:  # Insert defaults after creating table
                self.insert(
                    recipe['title'], recipe['author'],
                    recipe['ingredients'], recipe['time'],
                    recipe['skill'], recipe['description'],
                    recipe['tooltip'])
        # Below doesn't work if we want to only insert the defaults if the table is being created
        # cursor.execute('''
        #     CREATE TABLE IF NOT EXISTS recipes
        #     (title TEXT, author TEXT, ingredients TEXT, time INTEGER, skill INTEGER, description TEXT)''')
        cursor.close()

    def select(self):
        """
        Return all recipes in the database. Each list in recipes contains a
        title, author, ingredient list, time, skill, description, and tooltip.
        :return: List of lists
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM recipes')
        return cursor.fetchall()

    def insert(self, title, author, ingredients, time, skill, description, tooltip):
        """
        Insert a recipe entry into the database.
        :param title: String
        :param author: String
        :param ingredients: List
        :param time: Integer
        :param skill: Integer
        :param description: String
        :param tooltip: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = dict(zip(
            ['Title', 'Author', 'Ingredients', 'Time', 'Skill', 'Description', 'Tooltip'],
            [title, author, '\n'.join(ingredients), time, skill, description, tooltip]))
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO recipes
            (title, author, ingredients, time, skill, description, tooltip)
            VALUES (:Title, :Author, :Ingredients, :Time, :Skill, :Description, :Tooltip)
            ''', params)

        connection.commit()
        cursor.close()
        return True
