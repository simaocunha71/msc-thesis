from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Check that the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Sort the list
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = (None, None)

    # Iterate over the list to find the closest pair
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair


# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)  # No change, same number
# You can add more test cases as needed.  #


# Explanation:
# This function takes a list of numbers as input and returns a tuple of two numbers that are the closest to each other.
# The function first sorts the list of numbers. Then, it iterates over the sorted list to find the closest pair of numbers.
# The minimum difference between any two adjacent numbers in the list is the distance between the closest pair.
# If the list has duplicate numbers, the function returns the pair of duplicates as the closest pair.
# The function raises a ValueError if the input list has less than two elements.

# Time complexity: O(n log n) due to the sorting operation.
# Space complexity: O(1) as it only uses a constant amount of space.