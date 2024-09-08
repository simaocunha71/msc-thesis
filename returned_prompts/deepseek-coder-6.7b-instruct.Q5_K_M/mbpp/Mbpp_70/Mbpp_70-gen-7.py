
def get_equal(tuples):
    return all(len(t) == len(tuples[0]) for t in tuples)

assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""
This function uses a generator expression to check the length of each tuple in the given list of tuples. If all lengths are equal, the all() function will return True. If any tuple has a different length, all() will return False.
"""

# Question 2

