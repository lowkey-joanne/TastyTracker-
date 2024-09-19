from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Connect to SQLite database
engine = create_engine('sqlite:///recipe.db')
Base = declarative_base()

# Define the Recipe model
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    image_url = Column(String)
    ingredients = Column(String)
    instructions = Column(String)

# Create tables (if not already created)
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

def add_recipe():
    print("\nEnter the details for a new recipe:")
    recipe_id = int(input("Recipe ID: "))
    name = input("Name of the Recipe: ")
    image_url = input("Image URL: ")
    ingredients = input("Ingredients (separate by commas): ")
    instructions = input("Instructions: ")

    # Create a new Recipe object
    new_recipe = Recipe(
        id=recipe_id,
        name=name,
        image_url=image_url,
        ingredients=ingredients,
        instructions=instructions
    )

    # Add the new recipe to the session
    session.add(new_recipe)
    session.commit()
    print("\nRecipe added successfully!\n")

def list_recipes():
    recipes = session.query(Recipe).all()
    for recipe in recipes:
        print(f"ID: {recipe.id}, Name: {recipe.name}")

def view_recipe_details():
    recipe_id = int(input("Enter the Recipe ID to view details: "))
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    if recipe:
        print(f"ID: {recipe.id}")
        print(f"Name: {recipe.name}")
        print(f"Image URL: {recipe.image_url}")
        print(f"Ingredients: {recipe.ingredients}")
        print(f"Instructions: {recipe.instructions}")
    else:
        print("Recipe not found.")

def update_recipe():
    recipe_id = int(input("Enter the Recipe ID to update: "))
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    if recipe:
        recipe.name = input("New Name of the Recipe: ") or recipe.name
        recipe.image_url = input("New Image URL: ") or recipe.image_url
        recipe.ingredients = input("New Ingredients (separate by commas): ") or recipe.ingredients
        recipe.instructions = input("New Instructions: ") or recipe.instructions
        session.commit()
        print("\nRecipe updated successfully!\n")
    else:
        print("Recipe not found.")

def delete_recipe():
    recipe_id = int(input("Enter the Recipe ID to delete: "))
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    if recipe:
        session.delete(recipe)
        session.commit()
        print("\nRecipe deleted successfully!\n")
    else:
        print("Recipe not found.")

def main():
    while True:
        print("--- TastyTracker CLI ---")
        print("1. Add a new recipe")
        print("2. List all recipes")
        print("3. View recipe details")
        print("4. Update a recipe")
        print("5. Delete a recipe")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_recipe()
        elif choice == '2':
            list_recipes()
        elif choice == '3':
            view_recipe_details()
        elif choice == '4':
            update_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == '6':
            break
        else:
            print("\nInvalid choice, try again.\n")

if __name__ == "__main__":
    main()
