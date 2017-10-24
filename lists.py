# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    greatest = 0
    if len(list_of_numbers) > 0:
        for elem in list_of_numbers:
            if elem > greatest:
                greatest = elem
        return greatest
    return 0
        



print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0