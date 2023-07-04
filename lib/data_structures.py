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
    },
]

def get_names(spicy_foods):
    return [food_name['name'] for food_name in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [foods for foods in spicy_foods if foods['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    for foods in spicy_foods:
        print(f'{foods["name"]} ({foods["cuisine"]}) | Heat Level: {"🌶" *foods["heat_level"]}')
    
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
   for by_cuisine in spicy_foods:
       if by_cuisine['cuisine'] == cuisine:
           return by_cuisine

def print_spiciest_foods(spicy_foods):
    for foods in spicy_foods:
        if foods["heat_level"] > 5:
            print(f'{foods["name"]} ({foods["cuisine"]}) | Heat Level: {"🌶" *foods["heat_level"]}')

def get_average_heat_level(spicy_foods):
    return (sum([avg_spice['heat_level'] for avg_spice in spicy_foods]) / len(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
