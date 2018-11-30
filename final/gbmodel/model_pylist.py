"""
Data is stored as a list with the each entry being a list containing the
title, author, ingredients, time, skill, description, and tooltip.
"""
from datetime import date
from .Model import Model

class model(Model):
    def __init__(self):
        super().__init__()  # Set defaults
        self.recipes = []
        for recipe in self.defaults:
            self.insert(
                recipe['title'], recipe['author'],
                '\n'.join(recipe['ingredients']), recipe['time'],
                recipe['skill'], recipe['description'],
                recipe['tooltip'])

    def select(self):
        """
        Returns all recipes.
        :return: List of lists
        """
        return self.recipes

    def insert(self, title, author, ingredients, time, skill, description, tooltip):
        """
        Appends a new list of values representing a new recipe into recipes.
        :param title: String
        :param author: String
        :param ingredients: List
        :param time: Integer
        :param skill: Integer
        :param description: String
        :param tooltip: String
        :return: True
        """
        params = [title, author, ingredients, time, skill, description, tooltip]
        self.recipes.append(params)
        return True
