def interleave_lists(a, b, c):
    return [val for pair in zip(a, b, c) for val in pair]

# test
print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))

"""
Note:
The zip function is used to combine the three lists into pairs, and then the flattening is done using a list comprehension.
"""


"""
