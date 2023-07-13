# Programming Challenge: Factorial
# Create a function which takes one positive integer as its input and returns its factorial.
def get_factorial(num):
    countdown = num
    this_factorial = 1

    while countdown:
        this_factorial *= countdown
        countdown -= 1

    return this_factorial

# To make sure that your function works correctly, you should call it with the inputs 3, 4, and 5
# and print what is returned by those calls.  For those inputs, you should get 6, 24, and 120, respectively.

print(get_factorial(3), get_factorial(4), get_factorial(5))

#---SOLUTION---#
# # The argument fac_num's name is short for factorial number.
# def factorial(fac_num):
#     # The local variable returned will be used in the for loop used to calculate fac_num's
#     # factorial. To do this, it will be multiplied by decrementing values of
#     # fac_num. Since it will be multiplied, it was given the initial value of 1.
#     returned = 1
#     # By the end of this for loop, returned will have been reassigned fac_num's factorial.
#     for item in range(fac_num, 1, -1):
#         returned *= item
#
#     # returns returned, which now holds the value of fac_num's factorial
#     return returned
#
#
# print(factorial(3))  # 6
# print(factorial(4))  # 24
# print(factorial(5))  # 120
