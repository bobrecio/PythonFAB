# 1. use .fromkeys() to create a dictionary that has the 
# consonants from the alphabet as its keys and the string "consonant" 
# as the value for each of those keys.  
# Only use lower case letters for the consonants.  "y" counts 
# as a consonant for this exercise.  Use a for loop and the .items() 
# method to print each of those key: value pairs on a different line.  
# For example, the first 3 lines in the output should be the following:
# b consonant
# c consonant
# d consonant
consonants = {}.fromkeys("bcdfghjklmnpqrstvwxz", "consonant")
for item in consonants.items():
    print(item)

# 2. paste this dictionary into your .py file then pop and
#  print "Big Mac" from it
fast_food_items = {"McDonald's": "Big Mac", 
                   "Burger King": "Whopper", 
                   "Chick-fil-A": "Original Chicken Sandwich"}
# popped = fast_food_items.pop("McDonald's")
# print(popped)
print(fast_food_items.pop("McDonald's"))
# 3. use .popitem() to remove the last key: value pair from the dictionary assigned to 
# fast_food_items then print new fast_food_items dictionary.

popped_item = fast_food_items.popitem()
print(popped_item)
print(fast_food_items)

#---SOLUTION---#
# for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
#     print(key, value)
 
# fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
# print(fast_food_items.pop("McDonald's"))
 
# fast_food_items.popitem()
# print(fast_food_items)