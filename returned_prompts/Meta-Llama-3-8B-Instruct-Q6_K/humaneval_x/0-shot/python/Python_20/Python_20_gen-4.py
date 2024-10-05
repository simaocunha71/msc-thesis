from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers = sorted(numbers)
    min_diff = float('inf')
    closest_pair = (None, None)

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair
# This function takes a list of numbers as input, sorts it and then iterates over the list to find the pair with the smallest difference.
# The pair is then returned as a tuple. If the list contains duplicate elements, this function will return the first pair it finds.
# If you want to return all pairs of equal closest elements, you would need to modify this function.
# This function assumes that the input list is not empty. If the list can be empty, you should add a check for this at the beginning of the function.
# This function also assumes that the input list contains at least two elements. If the list can contain less than two elements, you should add a check for this at the beginning of the function.  # noqa: E501
# You can test this function using the following test cases:
# find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
# find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])  # noqa: E501
# These test cases should return the expected results.