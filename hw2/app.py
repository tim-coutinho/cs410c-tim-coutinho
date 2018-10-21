"""
A simple guestbook flask app.
"""
import flask
from flask.views import MethodView
from index import Index
from add_recipe import AddRecipe

app = flask.Flask(__name__)  # Our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/add_recipe/',
                 view_func=AddRecipe.as_view('add_recipe'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
