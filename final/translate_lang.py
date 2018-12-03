from flask import redirect, request, url_for, render_template
from flask.views import MethodView
from google.cloud import translate
import gbmodel

class TranslateLanguage(MethodView):
    def get(self):
        model = gbmodel.get_model()

        recipes = [
            dict(title = row[0],
            author = row[1],
            ingredients = row[2],
            time = row[3],
            skill = row[4],
            description = row[5])
            for row in model.select()
        ]
        text = "hello"
        print(self.translate_recipe(text, dest='ko'))
        return render_template('recipe_translate.html', recipes=recipes)

    def post(self):
        """
        """

    def translate_recipe(self, text, dest):
        """
        Translates the detected language and returns only the text result
        :param text: String
        :param dest: String
        """
        translate_client = translate.Client()
        translation = translate_client.translate(
            "text",
            target_language=dest)
        return translation.text

    def translate_ingredients(self, texts, dest):
        """
        Translates the detected language and returns only the text result
        :param text: String
        :param dest: String
        """
        # translator = Translator()
        # for text in texts:
        #     translated = translator.translate(text, dest)
        # return translated.text
