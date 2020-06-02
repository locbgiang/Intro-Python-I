q = [10, 20, 30, 40, 50, 60]

# python has a really nice slicing syntax
# if we want 3 and 4 from q

#print(q[2:4])

# we can just leave the left side of the colon out if
# we just want to start from the beginning of the list
#print(q[:4])

# we can also leave the right side if we just want
# the start up to the end
#print(q[4:])

# we can combine this slicing syntax with for loops
# we can just loop through the slice
for elem in q[:4]:
    print(elem)