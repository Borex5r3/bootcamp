# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adbaich <adbaich@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/02 03:14:56 by adbaich           #+#    #+#              #
#    Updated: 2022/03/04 01:01:11 by adbaich          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import os
cookbook = {
    "Sandwich_recipe": {
        "name": "sandwich",
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake_recipe": {
        "name": "cake",
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad_recipe": {
        "name": "salad",
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}
def add_recipe():
    name = input("Enter a name:\n>> ")
    new_recipe = dict(cookbook["Salad_recipe"].copy())
    new_recipe["name"] = name
    print("Enter ingredients:")
    new_recipe["ingredients"] = tuple(map(str ,(input("") for i in range(4))))
    new_recipe["meal"] = input("Enter a meal type:\n")
    new_recipe["prep_time"] = input("Enter a preparation time:\n")
    cookbook[f"{name.capitalize()}_recipe"] = new_recipe
def print_recipe_names():
    for recipe in cookbook:
        name = dict(cookbook[recipe].copy())
        print(name["name"])
def name_deatails(str):
    a = 0
    for recipe in cookbook:
        name = dict(cookbook[recipe].copy())
        check = name["name"]
        if str == check: 
            a += 1
            print("Recipe for {}:\n".format(str))
            print(" ingredients list: {}".format(name["ingredients"]))
            print(" To be eaten for {}.".format(name["meal"]))
            print(" Takes {} minutes of cooking.".format(name["prep_time"]))
    if a == 0:
        print("recipe wasn't found !")
def del_recipe(str):
    for recipe in cookbook:
        name = dict(cookbook[recipe].copy())
        check = name["name"]
        if check == str:
            cookbook.pop(recipe,"dict not found")
            break
print("Welcome to the Python Cookbook !\nList of available option:\n 1: Add a recipe\n 2: Delete a recipe\n 3: Print a recipe\n 4: Print the cookbook\n 5: Quit")
while 1:
    try:
        option = int(input("\nPlease select an option:\n>> "))
        if option == 1:
            add_recipe()
        elif option == 2:
            del_recipe(input("\nPlease enter a recipe name to delete it\n>> "))
        elif option == 3:
            name_deatails(input("\nPlease enter a recipe name to get its details:\n>> "))
        elif option == 4:
            print_recipe_names()
        elif option == 5:
            print("\nCookbook closed. Goodbye !")
            os._exit(0)
        else:
            print("\nSorry, this option does not exist.")
            print("\nWelcome to the Python Cookbook !\nList of available option:\n 1: Add a recipe\n 2: Delete a recipe\n 3: Print a recipe\n 4: Print the cookbook\n 5: Quit\n")
    except:
        print("\nSorry, this option does not exist.")
        print("\nWelcome to the Python Cookbook !\nList of available option:\n 1: Add a recipe\n 2: Delete a recipe\n 3: Print a recipe\n 4: Print the cookbook\n 5: Quit\n")
        continue

