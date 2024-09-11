"""
def and_tuples(t1, t2):
    """
    >>> and_tuples((10, 4, 6, 9), (5, 2, 3, 3))
    (0, 0, 2, 1)
    """
    # initialize result
    result = ()

    # get length of tuples
    n = len(t1)

    # traverse tuples and find elementwise
    for i in range(n):
        result += (t1[i] & t2[i],)

    # return result
    return result

if __name__ == '__main__':
    print(and_tuples((10, 4, 6, 9), (5, 2, 3, 3)))
"""

# Python3 program to find
# bitwise AND of two tuples

# Function to find bitwise AND
# of two tuples
def and_tuples(t1, t2):
    # Get length of tuples
    n = len(t1)

    # Initialize result
    result = ()

    # Traverse tuples and find
    # elementwise
    for i in range(n):
        result += (t1[i] & t2[i],)

    # Return result
    return result

# Driver code
if __name__ == '__main__':
    print(and_tuples((10, 4, 6, 9), (5, 2, 3, 3)))




















"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""