def check_smaller(t1, t2):
    """
    Check if each element of second tuple is smaller than its corresponding element in the first tuple.
    """
    return all(a < b for a, b in zip(t1, t2))

# Testing
assert check_smaller((1, 2, 3), (2, 3, 4)) == False


# Complexity
# Time complexity: O(n)
# Space complexity: O(1)





def check_smaller(t1, t2):
    """
    Check if each element of second tuple is smaller than its corresponding element in the first tuple.
    """
    if len(t1) != len(t2):
        return False
    return all(a < b for a, b in zip(t1, t2))

# Testing
assert check_smaller((1, 2, 3), (2, 3, 4)) == False


# Complexity
# Time complexity: O(n)
# Space complexity: O(1)



"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.

Explanation:
We can check if each element of second tuple is smaller than its corresponding element in the first tuple by using zip function to iterate over tuples simultaneously and checking if each element of the first tuple is smaller than its corresponding element in the second tuple.

Complexity:
Time complexity: O(n), where n is the length of the tuples. We only need to iterate over the tuples once.
Space complexity: O(1), as we don't need any extra space that grows with the input size.
"""


def check_smaller(t1, t2):
    """
    Check if each element of second tuple is smaller than its corresponding element in the first tuple.
    """
    if len(t1) != len(t2):
        return False
    return all(a < b for a, b in zip(t1, t2))

# Testing
assert check_smaller((1, 2, 3), (2, 3, 4)) == False


