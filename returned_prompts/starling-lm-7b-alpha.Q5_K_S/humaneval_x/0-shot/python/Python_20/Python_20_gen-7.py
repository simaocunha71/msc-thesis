def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Initialize variables
    closest_num = None
    closest_pair = None

    # Iterate through the numbers
    for i, num1 in enumerate(numbers):
        for num2 in numbers[i+1:]:
            # Find the closest pair
            if closest_pair is None or abs(num1 - num2) < abs(closest_pair[0] - closest_pair[1]):
                closest_pair = (num1, num2)

    # Return the closest pair
    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)

# More test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 3.0]))  # (3.0, 3.0)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 4.0]))  # (4.0, 4.0)
print