# 1.create a variable and assign it a dictionary that has 5 key value pairs
my_dictionary = {
    "fname":"Bob",
    "lname":"Recio",
    "email":"bobrecio@gmail.com",
    "empid":"562295",
    "userid":"bobrecio"
    }
# 2.print and access the value held at the third key in the dictionary
print(my_dictionary["email"])
# 3.use the in keyword to check if a key appears in the dictionary and print the result
print("a key" in my_dictionary)
# 4.use not in to check if a key does not appear in the dictionary and print the result
print("a key" not in my_dictionary)

#---SOLUTION---#
# example solution
dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(dictionary["c"])
print("a" in dictionary)
print("b" not in dictionary)