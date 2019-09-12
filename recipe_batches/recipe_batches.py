#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  max_batches = None
  for i in recipe:
    #Kinda ugly. Trying to figure out how
    #to remove check or place elsewhere.
    if i not in ingredients:
      return 0
    #Floor division rounds down to nearest whole number.
    #Divides through to see if valid recupe to ingredients.
    batches = (ingredients[i] // recipe[i])
    #Check to see the lowest possible amount of
    #batches with the ingredients at hand.
    if max_batches is None:
      max_batches = batches
    elif batches < max_batches:
      max_batches = batches
  return max_batches



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))