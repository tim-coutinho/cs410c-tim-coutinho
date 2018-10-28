"""
A simple flask app to keep track of recipes.
Data is stored in a SQLite database with the columns title, author,
ingredients, time, skill, and description.
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
                (title TEXT, author TEXT, ingredients TEXT, time INTEGER, skill INTEGER, description TEXT)''')
            for recipe in self.defaults:  # Insert defaults after creating table
                self.insert(
                    recipe['title'], recipe['author'],
                    recipe['ingredients'], recipe['time'],
                    recipe['skill'], recipe['description'])
        # Below doesn't work if we want to only insert the defaults if the table is being created
        # cursor.execute('''
        #     CREATE TABLE IF NOT EXISTS recipes
        #     (title TEXT, author TEXT, ingredients TEXT, time INTEGER, skill INTEGER, description TEXT)''')
        cursor.close()

    def select(self):
        """
        Return all recipes in the database. Each list in recipes contains a
        title, author, ingredient list, time, skill, and description.
        :return: List of lists
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM recipes')
        return cursor.fetchall()

    def insert(self, title, author, ingredients, time, skill, description):
        """
        Insert a recipe entry into the database.
        :param title: String
        :param author: String
        :param ingredients: String
        :param time: Integer
        :param skill: Integer
        :param description: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = dict(zip(
            ['Title', 'Author', 'Ingredients', 'Time', 'Skill', 'Description'],
            [title, author, ingredients, time, skill, description]))
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO recipes
            (title, author, ingredients, time, skill, description)
            VALUES (:Title, :Author, :Ingredients, :Time, :Skill, :Description)
            ''', params)

        connection.commit()
        cursor.close()
        return True
