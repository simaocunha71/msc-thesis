def find_Volume(base_area, height):
    """
    Find the volume of a triangular prism

    Parameters
    ----------
    base_area : int or float
        The area of the base of the triangle
    height : int or float
        The height of the triangular prism

    Returns
    -------
    int or float
        The volume of the triangular prism
    """
    return 0.5 * base_area * height


# Testing
assert find_Volume(10,8,6) == 240

# More tests
assert find_Volume(10,8,6) == 240
assert find_Volume(8,10,6) == 320
assert find_Volume(8,10,6) == 320
assert find_Volume(8,10,6) == 320
assert find_Volume(8,10,6) == 320

# Tests with random values
for _ in range(1000):
    import random
    base_area = random.uniform(1, 100)
    height = random.uniform(1, 100)
    assert abs(find_Volume(base_area, height) - 0.5 * base_area * height) < 10 ** -6

# Tests with extremes
assert find_Volume(0, 1) == 0
assert find_Volume(10 ** 100, 1) == 10 ** 100
assert find_Volume(1, 10 ** 100) == 10 ** 100

# Test with NaN
assert find_Volume(float('nan'), 1) == float('nan')
assert find_Volume(1, float('nan')) == float('nan')

# Test with infinity
assert find_Volume(1, float('inf')) == float('inf')
assert find_Volume(float('inf'), 1) == float('inf')


# Test with complex
assert find_Volume(1 + 2j, 1) == 1 + 2j

# Test with strings
assert find_Volume('1