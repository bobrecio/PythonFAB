# Programming Challenge: Grade Determiner
# Professor Fuentes teaches a Python class and uses the following grading scale for all of her exams.
# You work as a teacher's assistant and due to her busy schedule she has requested that you write a
# program which will determine the grades of the class's students.
#
# Her grading scale is as follows:
# A score of 90 or above is an A
#
# A score of 80 or above is a B
#
# A score of 70 or above is a C
#
# A score of 60 or above is a D
#
# A score any lower is an F
#
# For this exercise, start by creating a variable and assigning that variable a student's score as an
# integer using input().
student_score = int(input("What's the student's grade? "))
letter_grade = ""
# Then, using nested if and else statements and the following set of rules, determine and then display the
# student's grade along with their score using print().
#
# If the student's score is greater than or equal to 90, then the student will receive an A grade.
if student_score >= 90:
    letter_grade = "A"
# Otherwise, if the student's score is greater than or equal to 80, then the student will receive an B grade.
else:
    if student_score >= 80:
        letter_grade = "B"
# Otherwise, if the student's score is greater than or equal to 70, then the student will receive an C grade.
    else:
        if student_score >= 70:
            letter_grade = "C"
# Otherwise, if the student's score is greater than or equal to 60, then the student will receive an D grade.
        else:
            if student_score >= 60:
                letter_grade = "D"
# Otherwise, the student will receive an F grade.
            else:
                if student_score < 60:
                    letter_grade = "F"
# Make sure to run your program multiple times and test it with values for each 5 of the different grades
# to make sure that the correct output is displayed for any value entered as a student's score.
print ("Your grade is: " + letter_grade)

#-----
# SOLUTION
# score = int(input("Please enter the student's score. "))
#
# if score >= 90:
#     print("This student's score of " + str(score) + " is an A.")
# else:
#     if score >= 80:
#         print("This student's score of " + str(score) + " is a B.")
#     else:
#         if score >= 70:
#             print("This student's score of " + str(score) + " is a C.")
#         else:
#             if score >= 60:
#                 print("This student's score of " + str(score) + " is a D.")
#             else:
#                 print("This student's score of " + str(score) + " is a F.")