from flask import redirect, request, url_for, render_template
from flask.views import MethodView
from googletrans import Translator
import gbmodel


class TranslateLanguage(MethodView):
    def get(self):
        model = gbmodel.get_model()

        recipes = [
            dict(title = self.translate(row[0], dest='ja'), 
            author = self.translate(row[1], dest='ja'), 
            ingredients = self.translate_ingredients(row[2], dest='ja'),
            time = row[3],
            skill = row[4],
            description = self.translate(row[5], dest='ja'))
            for row in model.select()
        ]
        categories = [
            dict(time= self.translate('Time:', dest='ja'))
        ]
        return render_template('recipe_translate.html', recipes=recipes, categories=categories)

    def post(self):
        """
        """

    def translate(self, text, dest):
        """
        Translates the detected language and returns only the text result
        :param text: String
        :param dest: String
        """
        translator = Translator()
        translated = translator.translate(text, dest)
        return translated.text

    def translate_ingredients(self, texts, dest):
        """
        Translates the detected language and returns only the text result
        :param text: String
        :param dest: String
        """
        translator = Translator()
        for text in texts:
            translated = translator.translate(text, dest)
        return translated.text
