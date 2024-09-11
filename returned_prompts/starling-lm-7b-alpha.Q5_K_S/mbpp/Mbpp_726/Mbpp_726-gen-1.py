def multiply_elements(t):
    if len(t) == 0:
        return ()
    return tuple(map(lambda x: x[0] * x[1], zip(t[:-1], t[1:])))


def test_multiply_elements():
    assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)


def multiply_elements(t):
    if len(t) == 0:
        return ()
    return tuple(map(lambda x: x[0] * x[1], zip(t[:-1], t[1:])))


def test_multiply_elements():
    assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)


# Python program to multiply elements of the tuple
def multiply_elements(t):
    # If tuple is empty, return empty tuple
    if len(t) == 0:
        return ()
    # Create a list and add product of each pair of adjacent elements
    # of the tuple to it
    l = [t[i] * t[i + 1] for i in range(len(t) - 1)]
    # Convert the list to tuple
    return tuple(l)


# Driver program to test above function
t = (1, 5, 7, 8, 10)
print(multiply_elements(t))


# Time complexity of above function is O(n)
# where n is the length of the tuple
# Auxiliary space complexity is O(n)


def multiply_elements(t):
    if len(t) == 0:
        return ()
    l = [t[i] * t[i + 1] for i in range(len(t) - 1)]
    return tuple(l)


def test_multiply_elements():
    assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56