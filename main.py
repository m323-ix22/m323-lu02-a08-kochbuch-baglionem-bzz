import json
def load_recipe(json_string):
    """
    Diese Funktion nimmt einen JSON-String als Argument und wandelt ihn in ein Python-Dictionary um.
    :param json_string: Ein String, der ein Rezept im JSON-Format enthält.
    :return: Ein Dictionary, das das Rezept repräsentiert.
    """
    return json.loads(json_string)


def adjust_recipe(recipe, new_servings):
    """
    Diese Funktion passt die Mengenangaben eines Rezepts an eine neue Anzahl von Personen an.
    :param recipe: Ein Dictionary, das das Rezept enthält, einschließlich der Zutaten und Portionen.
    :param new_servings: Die neue Anzahl von Personen, für die das Rezept angepasst werden soll.
    :return: Ein neues Dictionary mit den angepassten Mengenangaben.
    """
    original_servings = recipe['servings']
    adjustment_factor = new_servings / original_servings

    adjusted_ingredients = {
        ingredient: quantity * adjustment_factor
        for ingredient, quantity in recipe['ingredients'].items()
    }

    adjusted_recipe = {
        'title': recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': new_servings
    }

    return adjusted_recipe


def adjust_recipe(recipe, new_servings):
    """
    Diese Funktion passt die Mengenangaben eines Rezepts an eine neue Anzahl von Personen an.
    :param recipe: Ein Dictionary, das das Rezept enthält, einschließlich der Zutaten und Portionen.
    :param new_servings: Die neue Anzahl von Personen, für die das Rezept angepasst werden soll.
    :return: Ein neues Dictionary mit den angepassten Mengenangaben.
    """
    original_servings = recipe['servings']
    adjustment_factor = new_servings / original_servings

    adjusted_ingredients = {
        ingredient: quantity * adjustment_factor
        for ingredient, quantity in recipe['ingredients'].items()
    }

    adjusted_recipe = {
        'title': recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': new_servings
    }

    return adjusted_recipe


# Dein Code kommt hier hin

if __name__ == '__main__':
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'

    recipe = load_recipe(recipe_json)
    print("Originales Rezept:", recipe)

    adjusted_recipe = adjust_recipe(recipe, 2)
    print("Angepasstes Rezept für 2 Personen:", adjusted_recipe)

    adjusted_recipe_6 = adjust_recipe(recipe, 6)
    print("Angepasstes Rezept für 6 Personen:", adjusted_recipe_6)
