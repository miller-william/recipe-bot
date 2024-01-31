import random
import csv

def load_recipes(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
    
def filter_recipes(recipes, criteria):
    filtered_recipes = []
    for recipe in recipes:
        # Check each criterion; if 'yes', then the corresponding CSV field should be 'TRUE'
        if all(criteria[key] == 'no' or (criteria[key] == 'yes' and recipe[key].upper() == 'TRUE') for key in criteria if key != 'return_random_recipe'):
            filtered_recipes.append(recipe)
    return filtered_recipes

def find_random_recipe(recipes, criteria):
    filtered = filter_recipes(recipes, criteria)
    return random.choice(filtered) if filtered else None