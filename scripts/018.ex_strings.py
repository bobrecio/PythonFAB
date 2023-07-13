# Strings Exercises
# Do all of this in a .py file in Pycharm

#1. Create a variable and assign it the string "Just do it!"
str_a = "Just do it!"
#2. Access the "!" from the variable by index and print() it
print(str_a[-1])
#3. Print the slice "do" from the variable
print(str_a[5:7])
#4. Get and print the slice "it!" from the variable
str_it = str_a[-3:]
print(str_it)
#5. Print the slice "Just" from the variable
print(str_a[:4])
#6. Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".
# Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.
str_dont = "Don't " + str_a[-6:]
print(str_dont)

# solution
# to_slice = "Just do it!"
# print(to_slice[10])   # prints "!"
# print(to_slice[5:7])  # prints "do"
# print(to_slice[8:])   # prints "it!"
# print(to_slice[:4])   # prints "Just"
# print("Don't " + to_slice[5:])  # prints "Don't do it!"