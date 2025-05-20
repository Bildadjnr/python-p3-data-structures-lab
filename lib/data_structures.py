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
    for spicy_food in spicy_foods:
        return [item["name"] for item in spicy_foods if "name" in item]

def get_spiciest_foods(spicy_foods):
    # foods_5 = []
    # for item in spicy_foods:
    #     if "heat_level" > 5:
    #         foods_5.append("name")
    #     return foods_5
    return [food for food in spicy_foods if food ["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emoji = food ["heat_level"] * "🌶"
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoji}")
    return food

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food ["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food ["heat_level"] > 5:
            heat_level_emoji = food ["heat_level"] * "🌶"
            print (f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoji}")

    return None
        


def get_average_heat_level(spicy_foods):
    total_heat_levels = [food['heat_level'] for food in spicy_foods]
    return sum (total_heat_levels) / len(total_heat_levels)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
