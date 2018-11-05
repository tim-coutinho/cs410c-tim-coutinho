"""
Python dictionary model
"""
from .Model import Model


class model(Model):
    def __init__(self):
        self.recipes = dict()
        defaults = [
            {
                'title': 'Default Recipe 1',
                'author': 'Abraham Lincoln',
                'ingredients': [
                    'Ingredient 1',
                    'Ingredient 2'
                ],
                'time': 15,
                'skill': 3,
                'description': 'Default description 1'
            },
            {
                'title': 'Default Recipe 2',
                'author': 'Tim Coutinho',
                'ingredients': [
                    'Ingredient 3',
                    'Ingredient 4',
                    'Ingredient 5',
                    'Ingredient 6'
                ],
                'time': 60,
                'skill': 9,
                'description': 'Default description 2'
            }
        ]
        for recipe in defaults:
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
        :param ingredients: List
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
