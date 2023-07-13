# Programming Challenge: Fizz Buzz
# Write a program that iterates over the integers 1 through 50 using a loop.
numbers = range(1,51)
# However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the output.
for num in numbers:
# For example, 15 is divisible by both 3 and 5, so instead of printing 15, print "FizzBuzz".
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} - FizzBuzz")
# For numbers which are multiples of 3 but not 5 (such as 42) print “Fizz” instead of the number.
    elif num % 3 == 0 and num % 5 != 0:
        print (f"{num} - Fizz")
# For the numbers that are multiples of 5 but not 3 (such as 20) print “Buzz” instead of the number.
    elif num % 3 !=  0 and num %  5 == 0:
        print (f"{num} - Buzz")
# All of the integers which are not multiples of 3 or 5 should just be printed as themselves.
    else:
        print(num)

#---SOLUTION---#
# for num in range(1, 51):
#     # If num is divisible by both 3 and 5, "FizzBuzz" will be printed.
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     # If num is only divisible by 3, "Fizz" will be printed.
#     elif num % 3 == 0:
#         print("Fizz")
#     # If num is only divisible by 5, "Buzz" will be printed.
#     elif num % 5 == 0:
#         print("Buzz")
#     # num itself will be printed in all other cases.
#     else:
#         print(num)