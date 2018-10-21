from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel


class AddRecipe(MethodView):
    def get(self):
        return render_template('add_recipe.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        args = request.form
        model.insert(
            args['title'], args['author'], args['ingredients'].split('\r\n'),
            int(args['time']), int(args['skill']), args['description'])
        return redirect(url_for('index'))
