#tuples

#make a list into a tuple
tuple_1 = tuple([3.14, 13, 49])
tuple_2 = tuple("abc")
print(tuple_1)
print(tuple_2)

#make a dictionary into a tuple;
# only KEYS are used
tuple_3 = tuple({"a":1, "b":2, "c":3})
print(tuple_3)

#indexing
tuple_4 = tuple([1,2,3,4,5,6,7,8,9,10])
print(tuple_4)
print(tuple_4[3]) #4
print(tuple_4[3:]) #4..10
print(tuple_4[2:5]) #3..5
print(tuple_4[:5]) #..6
print(tuple_4[-1]) #10

#tuples are immutable
#tuple_5[2] = "b" #ERROR

#tuples take up less memory; faster
list_6 = [11,22,33,44,55]
tuple_6 = (11,22,33,44,55)
print(list_6.__sizeof__())
print(tuple_6.__sizeof__())

