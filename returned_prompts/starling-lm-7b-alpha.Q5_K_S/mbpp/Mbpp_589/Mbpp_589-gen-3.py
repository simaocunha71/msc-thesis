def perfect_squares(start, end):
    result = []
    for i in range(start, end + 1):
        if i ** 0.5 == int(i ** 0.5):
            result.append(i)
    return result


def test_perfect_squares():
    assert perfect_squares(1, 30) == [1, 4, 9, 16, 25]


test_perfect_squares()

# This code defines a function called `perfect_squares` that takes in two parameters: `start` and `end`. It initializes an empty list called `result` to store the perfect squares. It then iterates through the range from `start` to `end + 1` and checks if the square root of `i` is equal to its integer value. If it is, then `i` is a perfect square and is appended to the `result` list. Finally, the function returns the `result` list.

# The code also includes a test function called `test_perfect_squares` that asserts the expected output of the `perfect_squares` function for the given input (`start` = 1, `end` = 30). This test ensures that the function is working correctly by comparing the actual output of the function with the expected output.

"""
Write a function to find perfect squares between two given numbers.
assert perfect_squ