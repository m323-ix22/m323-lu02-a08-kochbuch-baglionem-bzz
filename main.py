"""
Dieses Modul verwaltet Rezepte und passt Mengenangaben basierend auf der Anzahl der Personen an.
"""

import json


def load_recipe(json_string):
    """
    Diese Funktion nimmt einen JSON-String als Argument und wandelt ihn in ein Python-Dictionary um.
    :param json_string: Ein String, der ein Rezept im JSON-Format enthält.
    :return: Ein Dictionary, das das Rezept repräsentiert.
    """
    return json.loads(json_string)


def adjust_recipe(recipe_data, new_servings):
    """
    Diese Funktion passt die Mengenangaben eines Rezepts an eine neue Anzahl von Personen an.
    :param recipe_data: Ein Dictionary, das das Rezept enthält, einschließlich der Zutaten und Portionen.
    :param new_servings: Die neue Anzahl von Personen, für die das Rezept angepasst werden soll.
    :return: Ein neues Dictionary mit den angepassten Mengenangaben.
    """
    original_servings = recipe_data['servings']
    adjustment_factor = new_servings / original_servings

    adjusted_ingredients = {
        ingredient: quantity * adjustment_factor
        for ingredient, quantity in recipe_data['ingredients'].items()
    }

    adjusted_recipe_data = {
        'title': recipe_data['title'],
        'ingredients': adjusted_ingredients,
        'servings': new_servings
    }

    return adjusted_recipe_data


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = (
        '{"title": "Spaghetti Bolognese", '
        '\'ingredients\': {\'Spaghetti\': 400, \'Tomato Sauce\': 300, \'Minced Meat\': 500}, '
        '\'servings\': 4}'
    )

    # Rezept laden
    original_recipe = load_recipe(recipe_json)
    print('Originales Rezept:')
    print(json.dumps(original_recipe, indent=4))

    # Rezept für 2 Personen anpassen
    adjusted_recipe_2 = adjust_recipe(original_recipe, 2)
    print('\nAngepasstes Rezept für 2 Personen:')
    print(json.dumps(adjusted_recipe_2, indent=4))

    # Rezept für 6 Personen anpassen
    adjusted_recipe_6 = adjust_recipe(original_recipe, 6)
    print('\nAngepasstes Rezept für 6 Personen:')
    print(json.dumps(adjusted_recipe_6, indent=4))

