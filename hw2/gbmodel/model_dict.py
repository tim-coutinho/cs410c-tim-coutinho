"""
Data is stored in a dictionary with the title as the value and the keys
author, ingredients, time, skill, and description.
"""
from .Model import Model


class model(Model):
    def __init__(self):
        super().__init__()  # Set defaults
        self.recipes = dict()  # For storing recipes locally
        for recipe in self.defaults:
            self.insert(
                recipe['title'], recipe['author'],
                recipe['ingredients'], recipe['time'],
                recipe['skill'], recipe['description'])

    def select(self):
        """
        Returns recipe dictionary
        Each list in recipes contains: title, author, ingredient list, time,
                                       skill, description
        :return: List of lists
        """
        return [[
                 title,
                 self.recipes[title]['Author'],
                 self.recipes[title]['Ingredients'],
                 self.recipes[title]['Time'],
                 self.recipes[title]['Skill'],
                 self.recipes[title]['Description']]
                for title in self.recipes]

    def insert(self, title, author, ingredients, time, skill, description):
        """
        Appends a new list of values representing a new recipe into recipes
        :param title: String
        :param author: String
        :param ingredients: String
        :param time: Integer
        :param skill: Integer
        :param description: String
        :return: True
        """
        params = dict(zip(
            ['Author', 'Ingredients', 'Time', 'Skill', 'Description'],
            [author, ingredients, time, skill, description]))
        self.recipes[title] = params
        return True
