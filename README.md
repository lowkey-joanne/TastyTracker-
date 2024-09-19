## TASTY TRACKER CHALLENGE

  
 Welcome to TastyTracker challenge resipitory! This resipitory contains the implementataion for a project focused on building a command-line interface (CLI) to manage and track recipies using Python and SQLAlchemy ORM. 

## Table of content
 1. Challenge Overview
 2. Project Setup
 3. Code Structure
 4. Requirements
 5. Usage
 6. License

## Challenge Overview 
The goal of this challenge is to build a system that allows users to manage their favorite recipes in a database. The application supports adding, updating, viewing, and deleting recipes, and utilizes Python's SQLAlchemy ORM for database management.

## object relationship
 A Recipe has an ID, name, image URL, ingredients, and instructions.
 Users can perform CRUD (Create, Read, Update, Delete) operations on the recipes in the database.

## Deliverables
 You are required to:

 Implement a Python-based CLI to manage recipes.
 Ensure that users can interact with the database through the terminal.
 Store recipe details such as ID, name, image URL, ingredients, and instructions. 

## Project Setup
To get started with this project, follow these steps:

## Clone The Repository 
```
git clone git@github.com:lowkey-joanne/TastyTracker-.git
```
## Navigate to the Project Directory
```
cd tastytracker
```
## Activate the Virtual Environment
```
venv\Scripts\activate
```
1. Windows:
```
bash
venv\Scripts\activate
````
2. macOS/Linux:

```
bash
source venv/bin/activate
```


## Install Dependencies
```
pip install -r requirements 
```

## Code Structure
main.py: Contains the CLI logic to add, view, update, and delete recipes.
recipe.db: SQLite database for storing recipes.
README.md: This file.

## Requirements
 
1. id: A unique integer ID for each recipe.
2. name: A string representing the name of the recipe.
3. image_url: A string for the image URL of the recipe.
4. ingredients: A string containing a list of ingredients separated by commas.
5. instructions: A string containing the steps to prepare the recipe


## Methods
1. add_recipe(): Adds a new recipe to the database.
2. view_recipes(): Displays a list of all recipes.
3. view_recipe_details(recipe_id): Displays details of a specific recipe by ID.
4. update_recipe(recipe_id): Updates an existing recipe.
5. delete_recipe(recipe_id): Deletes a recipe by its ID.

## Usage
1. Run the CLI:
```
python main.py
```
2. Follow the prompts to interact with the TastyTracker system:
Add a new recipe
1. List all recipes
2. View details of a specific recipe
3. Update or delete a recipe

## License
This project is licensed under the MIT License.

