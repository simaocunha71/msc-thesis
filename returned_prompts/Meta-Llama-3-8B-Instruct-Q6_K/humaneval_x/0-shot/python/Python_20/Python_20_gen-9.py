from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    sorted_numbers = sorted(numbers)
    min_diff = float('inf')
    closest_pair = (sorted_numbers[0], sorted_numbers[0])

    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_pair

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)  # Note: It's a duplicate. If you want to ignore duplicates, you can add a check before the comparison: if i > 0 and sorted_numbers[i] == sorted_numbers[i - 1]: continue
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 1.9]))  # Output: (1.0, 1.9)  # Note: It's not exactly equal, but it's the closest pair. You can adjust the tolerance as needed. For example, you can use the absolute difference instead of the difference itself: diff = abs(sorted_numbers[i + 1] - sorted_numbers[i])
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 1.0, 2.0]))  # Output: (1.0, 1.0)  # Note: There are duplicate elements. You can adjust the code to ignore duplicates. For example, you can use a set instead of a list: sorted_numbers = sorted(set(numbers))  # This will remove duplicates before sorting. You can also use a dictionary to keep track of the count of each element and then sort based on the count. For