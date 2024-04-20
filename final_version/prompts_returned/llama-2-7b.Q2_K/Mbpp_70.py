"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""

def get_equal(tuples):
    return all([tuple in sorted(set(tuples)) for tuple in tuples])
    
if __name__ == '__main__':
	print get_equal([(11,22),(44,55)])