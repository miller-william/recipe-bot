from flask import Flask, request, jsonify
from flask_cors import CORS
# Testing
from dotenv import load_dotenv
import os
import ast

from utils.recipe_utils import load_recipes, filter_recipes, find_random_recipe

#openai and langchain setup
from langchain.chat_models import ChatOpenAI

from langchain.schema import HumanMessage, SystemMessage

def is_valid_dict_format(s):
    # Basic structural checks
    if not (s.startswith('{') and s.endswith('}')):
        if not (s.startswith('[{') and s.endswith('}]')):
            return False

    try:
        # Try safely evaluating the string
        ast.literal_eval(s)
        return True
    except (ValueError, SyntaxError):
        # Not a valid Python literal
        return False

load_dotenv() #for local run
openai_api_key = os.environ.get("OPENAI_API_KEY")


# Get the current working directory
current_directory = os.getcwd()

chat = ChatOpenAI(temperature=0)



######## Flask app ###########

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

#import recipes
recipes = load_recipes('data/recipes.csv')

@app.route('/message', methods=['POST'])
def reply_message():
    data = request.json
    user_message = data.get('message', '').lower()

    # Set up openAI prompt
    messages = [
        SystemMessage(
            content="""You are a recipe bot. Your only purpose is to help to identify whether the user wants a selection of random recipes and what their requirements are. 
            All your responses should be related to this goal.
             
            First, determine whether the user wants you to select a random recipe and how many recipes they want.  Check if you are not sure.
            
            Then determine if they have any of the following requirements for their recipes:
            - vegetarian (for vegetarian only dishes)
            - healthy (for healthier dishes)
            - pasta (for pasta based dishes)
            - rice (for rice based dishes)
            - noodles (for noodle based dishes)
            - easy (for easy to make recipes)
            - cheesy (for dishes containing lots of cheese)
            
            Once you have these requirements, return a response in the following format (a list of dictionaries relating to each recipe):
            [{'return_random_recipe': 'yes',
            'vegetarian' : 'yes/no',
            'healthy' : 'yes/no',
            'pasta' : 'yes/no',
            'rice' : 'yes/no',
            'noodles' : 'yes/no',
            'easy' : 'yes/no',
            'cheesy' : 'yes/no'}]

            For example, if the user asks for 3 recipes, there should be three elements in this list.

            If you are going to provide a response in this format - it is VERY important not to provide any other text apart from this formatted text.
            
            If they don't have any requirements, you can assume 'no' to all the requirements.  

            If they ask you to pick the requirements, just select a single criteria to be 'yes'.
            """ 
        ),
        HumanMessage(
            content=user_message
        ),
    ]
    output = chat(messages)  #calling the OpenAI API
    output_string = output.content
    print(f"OpenAI response: {output}")

    # If we have a dict list of requirements returned by the chatbot
    if is_valid_dict_format(output_string):
        criteria = ast.literal_eval(output_string)
        if len(criteria) == 1:
            criteria = criteria[0]
            random_recipe = find_random_recipe(recipes, criteria)
            print(random_recipe)

            return jsonify({'reply': f"You should have: {random_recipe['meal'].capitalize()}"}) if random_recipe else jsonify({'reply': 'Sorry - no matching recipes available.'})
        
        if len(criteria) > 1:
            # need to create a list of random recipes
            multiple_recipes = []
            filtered_recipes = recipes.copy()
            for c in criteria:
                random_recipe = find_random_recipe(filtered_recipes, c)
                multiple_recipes.append(random_recipe)
                filtered_recipes = [recipe for recipe in filtered_recipes if recipe['meal'] != random_recipe['meal']]
            # construct string
            multiple_output = "Sure! Here are your recipes:" 
            for recipe in multiple_recipes:
                multiple_output = multiple_output + f"\n -{recipe['meal'].capitalize()}"

            return jsonify({'reply': multiple_output})

    return jsonify({'reply': output.content})

@app.route('/')
def home():
    return "Flask backend is running!"

if __name__ == '__main__':
    app.run(debug=True)
