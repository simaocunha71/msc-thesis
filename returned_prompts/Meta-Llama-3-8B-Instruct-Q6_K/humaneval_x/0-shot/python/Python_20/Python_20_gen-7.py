from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")
    numbers.sort()
    closest_pair = (numbers[0], numbers[1])
    min_diff = abs(numbers[1] - numbers[0])

    for i in range(1, len(numbers) - 1):
        diff = abs(numbers[i + 1] - numbers[i])
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test cases:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
# Test case for edge case
print(find_closest_elements([1.0, 1.0, 1.0]))  # (1.0, 1.0)
# Test case for edge case
print(find_closest_elements([1.0]))  # raises ValueError
# Test case for edge case
print(find_closest_elements([]))  # raises ValueError
# Test case for edge case
print(find_closest_elements([1.0, 2.0]))  # (1.0, 2.0)
# Test case for edge case
print(find_closest_elements([1.0, 2.0, 3.0]))  # (2.0, 3.0)
# Test case for edge case
print(find_closest_elements([1.0, 2.0, 3.0, 4.0]))  # (3.0, 4.0)
# Test case for edge case
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]))  # (4.0, 5.0)
# Test case for edge case
print(find_closest_elements([1.0, 2.0, 3.0, 4.0,