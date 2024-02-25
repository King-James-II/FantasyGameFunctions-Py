# Program: Fantasy Adventure: Function Excitement
# Description: This Python program simulates a fantasy adventure where a brave hero embarks on thrilling quests,
# encounters enemies, and discovers hidden treasure. It demonstrates the usage of functions with and without arguments,
# return and void statements, as well as the utilization of standard modules.

# Define a function without arguments and return statement
def greet_hero():
    # Function to greet the hero and prepare for the adventure
    print("Greetings, brave hero!")
    print("Prepare yourself for a thrilling adventure!")

# Define a function with arguments and return statement
def calculate_attack_damage(weapon_power, enemy_armor):
    # Function to calculate the damage inflicted during an attack
    damage = weapon_power - enemy_armor
    return max(damage, 0)  # Ensure damage is non-negative

# Define a function with arguments and void statement
def attack_enemy(hero_name, enemy_type):
    # Function to simulate an attack on an enemy
    print(f"{hero_name} bravely attacks the {enemy_type}!")

# Define a function that uses a standard module
def find_hidden_treasure():
    # Function to randomly determine if hidden treasure is found
    import random
    treasure_found = random.choice([True, False])
    return treasure_found

# Main function to start the adventure
def embark_on_adventure():
    # Call the function without arguments
    greet_hero()
    
    # Call the function with arguments and return statement
    hero_weapon_power = 50
    enemy_armor_strength = 20
    damage_inflicted = calculate_attack_damage(hero_weapon_power, enemy_armor_strength)
    print(f"The hero inflicts {damage_inflicted} damage on the enemy!")
    
    # Call the function with arguments and void statement
    hero_name = "Sir Galahad"
    enemy_type = "Dragon"
    attack_enemy(hero_name, enemy_type)
    
    # Call the function that uses a standard module
    if find_hidden_treasure():
        print("The hero discovers hidden treasure!")
    else:
        print("The hero searches in vain for hidden treasure.")

# Let the adventure begin!
if __name__ == "__main__":
    embark_on_adventure()
