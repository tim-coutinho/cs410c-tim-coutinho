from flask import redirect, request, url_for, render_template
from flask.views import MethodView
from google.cloud import translate
import gbmodel

class TranslateLanguage(MethodView):
    def get(self):
        model = gbmodel.get_model()

        recipes = [
            dict(title=self.translate_recipe(row[0]),
            author=row[1],
            ingredients=self.translate_ingredients(row[2].split('\n')),
            time=row[3],
            skill=row[4],
            description=self.translate_recipe(row[5]),
            tooltip=self.translate_recipe(row[6]))
            for row in model.select()
        ]
        return render_template('recipe_translate.html', recipes=recipes)

    def translate_recipe(self, text):
        """
        Translates the detected language and returns the translatedText result in spanish
        :param text: String
        """
        translate_client = translate.Client(target_language='es')
        translation = translate_client.translate(text)
        return translation.get('translatedText')

    def translate_ingredients(self, texts):
        """
        Translates the detected language and returns only the dict result in spanish
        :param texts: String
        """
        translate_client = translate.Client(target_language='es')
        translation = translate_client.translate(texts)
        return translation