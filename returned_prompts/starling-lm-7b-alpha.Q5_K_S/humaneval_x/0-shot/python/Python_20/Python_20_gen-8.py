def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    min_diff = float("inf")
    first_closest = None
    second_closest = None
    for i in range(len(numbers)-1):
        if abs(numbers[i] - numbers[i+1]) < min_diff:
            min_diff = abs(numbers[i] - numbers[i+1])
            first_closest = numbers[i]
            second_closest = numbers[i+1]
    return first_closest, second_closest


def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)


test_find_closest_elements()

# To make this code pass the tests below, define the function find_closest_elements:


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Your code here
    pass


# After defining the function, run the tests to verify it works correctly.
# Note that the tests provided here are just a few examples, and you should write your own tests to ensure the function
# works correctly for all possible inputs.
# To run the tests, copy the `test_find_closest_elements` function at the end of the file and paste it at the top of the file,
# before the `find_closest_elements` function definition.

# After pasting the `test_find_closest_elements` function at the top of the file, run it to verify the function works correctly:
# >>> test_find_closest_elements()


# Note: The `from __future__ import annotations` statement at the top of the file is necessary to support assignment in
# function return type