from flask import render_template
from flask.views import MethodView
import gbmodel


class Recipes(MethodView):
    def get(self):
        """
        Get the model and return all entries in the recipe list.
        :return: HTML template with the recipes passed in as a parameter
        """
        model = gbmodel.get_model()
        recipes = [
            dict(title=row[0], author=row[1], ingredients=row[2].split('\n'),
                 time=row[3], skill=row[4], description=row[5])
            for row in model.select()
        ]
        return render_template('recipes.html', recipes=recipes)
