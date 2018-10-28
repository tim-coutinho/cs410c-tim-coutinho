class Model():
    def __init__(self):
        self.defaults = [
            {
                'title': 'Default Recipe 1',
                'author': 'Abraham Lincoln',
                'ingredients': 'Ingredient 1\nIngredient 2',
                'time': 15,
                'skill': 3,
                'description': 'Default description 1'
            },
            {
                'title': 'Default Recipe 2',
                'author': 'Tim Coutinho',
                'ingredients': 'Ingredient 3\nIngredient 4\nIngredient 5\nIngredient 6',
                'time': 60,
                'skill': 9,
                'description': 'Default description 2'
            }
        ]

    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, name, email, message):
        """
        Inserts entry into database
        :param title: String
        :param author: String
        :param ingredients: List
        :param time: Integer
        :param skill: Integer
        :param description: String
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass
