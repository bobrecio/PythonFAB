# string methods 2 exercises
# Do all of this in a .py file:
#
# Create a variable called the_string and assign it the string "North Dakota".
#
# Call .rjust() on the_string with 17 as its argument and print() the result.
#
# Call .ljust() on the_string with the arguments 17 and "*" then print() the result.
#
# Create a variable called center_plus and assign it the result of .center() being called on the_string with 16 and "+" as arguments.
#
# Use print() to display the string assigned to center_plus.
#
# Call .lstrip() on the_string to remove "North" then print() the result.
#
# Call .rstrip() on center_plus with "+" as its argument and print() the result.
#
# Call .strip() on center_plus with "+" as its argument and print() the result.
#
# Call .replace() on the_string and replace "North" with "South".  print() the result.

#---SOLUTION---#
the_string = "North Dakota"
print("the_string.rjust(17,'.') -> " + the_string.rjust(17,'.'))
print("the_string.ljust(17, '.') -> " + the_string.ljust(17, "."))
center_string = the_string.center(16, ".")
print("the_string.center(16, '.') -> " + center_string)
print("the_string.lstrip('North') -> " + the_string.lstrip("North"))
print("center_string.rstrip('.') -> " + center_string.rstrip("."))
print("center_string.strip('.') -> " + center_string.strip("."))
print("the_string.replace('North', 'South') -> " + the_string.replace("North", "South"))