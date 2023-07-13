# del and list methods exercises
# Do all of this in a .py file in Pycharm.
# 1.Create a variable called arctic_animals and assign it the list ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
print(arctic_animals)
# 2.Use del to remove "tiger" from the list assigned to arctic_animals.
del arctic_animals[4]
print(arctic_animals)
# 3.Use the .remove() method to remove the string "elephant" from the list assigned to arctic_animals.
arctic_animals.remove("elephant")
print(arctic_animals)
# 4.Use the .append() method to add the string "arctic fox" to the list arctic_animals.
arctic_animals.append("arctic fox")
print(arctic_animals)
# 5.Use .insert() to insert the string "snowy owl" between the strings "polar bear" and "walrus" inside of arctic_animals.
arctic_animals.insert(2,"snowy owl")
print(arctic_animals)
# 6.Use the .sort() method to rearrange the strings in arctic_animals into alphabetical order.
arctic_animals.sort()
# 7.Use print() to display the list assigned to arctic_animals
print(arctic_animals)
# 8.Use .index() to get the index number of "reindeer" from arctic_animals then print it.
print(arctic_animals.index("reindeer"))
# 9.Use .pop() to get the last item from the list arctic_animals then print it.
arctic_animals.pop()
print(arctic_animals)

#---SOLUTION---#
# arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
# del arctic_animals[4]
# arctic_animals.remove("elephant")
# arctic_animals.append("arctic fox")
# arctic_animals.insert(2, "snowy owl")
# arctic_animals.sort()
# print(arctic_animals)
# print(arctic_animals.index("reindeer"))
# print(arctic_animals.pop())