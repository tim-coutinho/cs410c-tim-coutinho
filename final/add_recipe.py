import json
import requests
from flask import redirect, request, url_for, render_template
from flask.views import MethodView

import gbmodel


class AddRecipe(MethodView):
    def get(self):
        return render_template('add_recipe.html')

    def post(self):
        """
        Accepts POST requests, and processes the form.
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        args = request.form
        ingredients = args['ingredients'].split('\r\n')
        url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
        query = json.dumps({'query': ', '.join(ingredients)})
        headers = {
            'x-app-key': '4a900d29f6416233ec26668100c24dc2',
            'Content-Type': 'application/json',
            'x-app-id': '0f3a292c'
        }
        res = requests.post(url, headers=headers, data=query)
        if res.ok:
            tooltip = self.get_nutrition(json.loads(res.text)['foods'])
        else:
            tooltip = 'Error acquiring nutritional information.'

        model.insert(
            args['title'], args['author'], ingredients, int(args['time']),
            int(args['skill']), args['description'], tooltip)
        return redirect(url_for('index'))

    def get_nutrition(self, foods):
        calories = protein = carbs = fat = 0
        for food in foods:
            calories += food['nf_calories']
            protein += food['nf_protein']
            carbs += food['nf_total_carbohydrate']
            fat += food['nf_total_fat']

        return 'Calories: {}\nProtein: {}g\nCarbs: {}g\nFat: {}g'.format(round(calories), round(protein), round(carbs), round(fat))
