# int() exercise
# In a Python file, use input() to ask the user to enter an integer that 10 will be added to.
# Assign what they type to a variable.
# print() the sum of the integer they entered and 10.

user_number = int(input("Enter an integer that will be added to 10... "))
user_num_plus_10 = 10 + user_number
print("The sum of " + str(user_number) + " and 10 is " + str(user_num_plus_10))

# Solution 1 (preferred):
#
# use_int = int(input("Please enter an integer.")) # make it an integer right away, to avoid confusion
# print(use_int + 10)
#
# Solution 2:
#
# use_int = input("Please enter an integer.")
# print(int(use_int) + 10) # remember to convert the input to an integer whenever you want to use it
