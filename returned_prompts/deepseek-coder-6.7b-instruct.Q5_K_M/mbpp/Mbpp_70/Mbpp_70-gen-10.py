
def get_equal(tuples):
    length = len(tuples[0])
    for tup in tuples:
        if len(tup) != length:
            return False
    return True

print(get_equal([(11, 22, 33), (44, 55, 66)]))  # True

# Alternative solution

def get_equal(tuples):
    return all(len(tup) == len(tuples[0]) for tup in tuples)

print(get_equal([(11, 22, 33), (44, 55, 66)]))  # True
"""

# Solution
def get_equal(tuples):
    length = len(tuples[0])
    for tup in tuples:
        if len(tup) != length:
            return False
    return True

print(get_equal([(11, 22, 33), (44, 55, 66, 77)]))  # False
print(get_equal([(11, 22, 33), (44, 55, 66)]))  # True
"""

# Alternative solution

def get_equal(tuples):
    return all(len(tup) == len(tuples[0]) for tup in tuples)

print(get_equal([(11, 22, 33), (44, 55, 66, 77)]))  # False
print(get_equal([(11, 22, 33), (44, 55, 66)]))  # True
"""
<jupyter_output>
False
True
<jupyter_text>
**Question 2**
<jupyter_code>
"""
