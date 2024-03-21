# dwarves = ["Dopey", "Grumpy", "Bashful"]

def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves):
        print((f"{index+1}. {dwarf}"))

# roll_call_dwarves(dwarves)

# planeteer_calls = ["earth", "wind", "fire", "water", "heart"]

def summon_captain_planet(planeteer_calls):
    return [f"{word.capitalize()}!" for word in planeteer_calls]

# print(summon_captain_planet(planeteer_calls))

# assorted_words = ["two", "go", "industrious", "bop"]

def long_planeteer_calls(assorted_words):
    return any(word for word in assorted_words if len(word) > 4)

# print(long_planeteer_calls(assorted_words))

# snacks = ["crackers", "gouda", "thyme"]
# soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
# ingredients = ["garlic", "rosemary", "bread"]

def find_the_cheese(list):
    gouda_present = [cheese for cheese in list if cheese == "gouda"] 
    camembert_present = [cheese for cheese in list if cheese == "camembert"] 
    cheddar_present = [cheese for cheese in list if cheese =="cheddar"] 
    if "".join(gouda_present) == "gouda":
        return "".join(gouda_present)
    elif "".join(camembert_present) == "camembert":
        return "".join(camembert_present)
    elif "".join(cheddar_present) == "cheddar":
        return "".join(cheddar_present)
    else:
        return None

# print(find_the_cheese(ingredients))
