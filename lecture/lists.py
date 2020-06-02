# create an empty list
# set the empty list to a variable p
p = []

# create a list with numbers
q = [ 1, 2, 3, 4, 5, 6]

# add a number to our q list

# where is the appended value getting added to the list?
#print(q)

# `append` method add

# what if we append to the beginning of a list?
q.insert(0, 90)

#print(q)

#############################################################################################
# how to print out all of the elements of a list
# let's use a for loop to do this

#for elem in q:
#    print(elem)

#############################################################################################
# combine our above loop with string interpolation
# to print a short message with each list element

#for elem in q:
#    print(f'element: {elem}')

#############################################################################################
# print each list element with a short message that
# also tells us in the element's index in the list
# the `enumerate` function gives us access to each
# list element as well as its index

#for i, elem, in enumerate(q):
#    print(f'index: {i}, element: {elem}')

#############################################################################################
# `_` in python denotes 'im tossing this value'

#for _ in q:

#############################################################################################
# in python, how do we loop a certain number of times?
# we can use the `range` function for this
# range(start=0, end, step=1)
# range is exclusive on the `end`

#for num in range(1, 11):
#    print(num)

#############################################################################################
# use `range` in conjunction with lists to iterate
# over the length of a list:
#for index in range(len(q)):
#    print(q[index])


#############################################################################################
# how do you loop through a range backwards?
# if we want to loop from 10 down to 1

for i in range(10, 0, -1):
    print(i)
