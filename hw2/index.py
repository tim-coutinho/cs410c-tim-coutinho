from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        recipes = [
            dict(title=row[0], author=row[1], ingredients=row[2],
                 time=row[3], skill=row[4], description=row[5])
            for row in model.select()
        ]
        return render_template('index.html', recipes=recipes)
