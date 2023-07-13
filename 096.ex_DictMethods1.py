# Dictionary Methods 1 - exercise

# 1.create a variable and assign it the following dictionary:

dict1 = {"Queen": "Bohemian Rhapsody", 
         "Bee Gees": "Stayin' Alive", 
         "U2": "One", 
         "Michael Jackson": "Billie Jean", 
         "The Beatles": "Hey Jude", 
         "Bob Dylan": "Like A Rolling Stone"}

# 2.make the dictionary span multiple lines so that the line the dictionary starts on is not too long.

# 3.print the length of the dictionary.
print(len(dict1))

# 4.use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines.
for key in dict1.keys():
    print(key)

# 5.print all of the values from the dictionary using the .values() method.
for value in dict1.values():
    print(value)

# 6.use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.
for item in dict1.items():
    print(item)

# 7.use the .get() method to check the dictionary for the key
# "Promise of the Real"
# and create a message that will print if the key is not found in the dictionary.
print(dict1.get("U2", "The key was not found"))

#---SOLUTION---#
# famous_songs = {"Queen": "Bohemian Rhapsody",
#                 "Bee Gees": "Stayin' Alive",
#                 "U2": "One",
#                 "Michael Jackson": "Billie Jean",
#                 "The Beatles": "Hey Jude",
#                 "Bob Dylan": "Like A Rolling Stone"}  # 1 and 2
# print(len(famous_songs))  # 3
# for key in famous_songs.keys():  # 4
#     print(key)
# print(famous_songs.values())  # 5
# for key, value in famous_songs.items():  # 6
#     print(key, value)
# print(famous_songs.get("Promise of the Real", "That is not a key that appears in the dictionary."))  # 7