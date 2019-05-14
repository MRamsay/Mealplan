import json


def format_ingredient(ingredient):

    rm_nulls = lambda x: x if x else ""

    quantity = rm_nulls(ingredient["quantity"])
    unit = rm_nulls(ingredient["unit"])

    quantityf = " (no unit)"

    if quantity or unit:
        quantityf = f' - {unit} {quantity}'

    return f'+ {ingredient["name"]}{quantityf}\n'

def recipe_to_string(recipe):
    title = f"## {recipe['name'].title()}"
    
    ingredients = ''.join(format_ingredient(i) for i in recipe["ingredients"])

    return f"""{title}
    
{ingredients}


    """


with open("recipes.json") as infile:
    data = json.load(infile)

    print("# Recipes")

    for recipe in data:
        print(recipe_to_string(recipe))
