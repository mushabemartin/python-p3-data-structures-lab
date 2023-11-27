spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    }
]

# Function to get names of spicy foods
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# Function to get spiciest foods
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# Function to print spicy foods with emojis representing heat level
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

# Function to get spicy food by cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next((food for food in spicy_foods if food["cuisine"] == cuisine), None)

# Function to print spiciest foods with heat level greater than 5
def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

# Function to get average heat level
def average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    return total_heat_level // len(spicy_foods)
