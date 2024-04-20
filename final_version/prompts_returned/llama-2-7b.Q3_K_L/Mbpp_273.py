"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""

def substract_elements(tuple1, tuple2):
    for i in range(len(tuple1)):
        if tupe1[i] < tupe2[i]:
            return 0
        else:
            return -1
