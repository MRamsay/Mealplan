import json


def format_ingredient(ingredient):
    
    return f'+ {ingredient["name"]} - {ingredient["quantity"]} {ingredient["unit"]}\n'

def recipe_to_string(recipe):
    title = f"# {recipe['name'].title()}"
    
    ingredients = ''.join(format_ingredient(i) for i in recipe["ingredients"])

    return f"""{title}
    
{ingredients}


    """


with open("recipes.json") as infile:
    data = json.load(infile)

    for recipe in data:
        print(recipe_to_string(recipe))
