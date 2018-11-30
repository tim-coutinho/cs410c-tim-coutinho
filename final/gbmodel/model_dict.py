"""
Python dictionary model
"""
from .Model import Model


class model(Model):
    def __init__(self):
        super().__init__()
        self.recipes = dict()
        for recipe in self.defaults:
            self.insert(
                recipe['title'], recipe['author'],
                recipe['ingredients'], recipe['time'],
                recipe['skill'], recipe['description'],
                recipe['tooltip'])

    def select(self):
        """
        Returns recipe dictionary
        Each list in recipes contains: title, author, ingredient list, time,
                                       skill, description, tooltip
        :return: List of lists
        """
        return [[
                 title,
                 self.recipes[title]['Author'],
                 '\n'.join(self.recipes[title]['Ingredients']),
                 self.recipes[title]['Time'],
                 self.recipes[title]['Skill'],
                 self.recipes[title]['Description'],
                 self.recipes[title]['Tooltip']]
                for title in self.recipes]

    def insert(self, title, author, ingredients, time, skill, description, tooltip):
        """
        Appends a new list of values representing a new recipe into recipes
        :param title: String
        :param author: String
        :param ingredients: List
        :param time: Integer
        :param skill: Integer
        :param description: String
        :param tooltip: String
        :return: True
        """
        params = dict(zip(
            ['Author', 'Ingredients', 'Time', 'Skill', 'Description', 'Tooltip'],
            [author, ingredients, time, skill, description, tooltip]))
        self.recipes[title] = params
        return True
