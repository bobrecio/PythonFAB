# dictionary methods 3 exercises

# 1.paste these 2 dictionaries into your file

internet_celebrities = {"DrDisrespect": "YouTube", 
                        "ZLaner": "Facebook", 
                        "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}

# 2.use .update() to add the contents of another_one to 
# internet_celebrities.
internet_celebrities.update(another_one)

# 3.create a variable and assign it a copy of 
# internet_celebrities.
internet_celebrities_copy = internet_celebrities.copy()

# 4.use the .clear() method to get rid of the contents of 
# internet celebrities.
internet_celebrities.clear()

# 5.print internet_celebrities.
print(internet_celebrities)

# 6.print the variable you created in step 3.1.
print(internet_celebrities_copy)

#---SOLUTION---#
# internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# another_one = {"shroud": "Twitch"}
# internet_celebrities.update(another_one)  # 2
# gamers = internet_celebrities.copy()  # 3
# internet_celebrities.clear()  # 4
# print(internet_celebrities)  # 5
# print(gamers)  # 6