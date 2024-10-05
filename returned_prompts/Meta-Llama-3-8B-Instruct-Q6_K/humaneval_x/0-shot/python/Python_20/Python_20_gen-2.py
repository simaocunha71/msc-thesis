from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    min_diff = float('inf')
    closest_pair = (None, None)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[i], numbers[j])

    return tuple(sorted(closest_pair))  # Ensure the pair is in ascending order
# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
# Time complexity: O(n^2)
# Space complexity: O(1)
# Note: The above solution assumes that the list contains at least two elements. If the list can be empty or contain only one element, you should add error checking code.  # noqa: E501
# Another approach is using the `sorted` function with a custom key function that calculates the absolute difference between two elements.  # noqa: E501
# This approach would have a time complexity of O(n log n) and a space complexity of O(n).  # noqa: E501
# Here is the code for the alternative approach:
# def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
#     sorted_numbers = sorted(numbers)
#     min_diff = float('inf')
#     closest_pair = (None, None)
#
#     for i in range(len(sorted_numbers) - 1):
#         diff = sorted_numbers[i + 1] - sorted_numbers[i]
#         if diff < min_diff:
#             min_diff = diff
#             closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
#
#     return tuple(sorted(closest_pair))  # Ensure the pair is in ascending order
# # Test cases
# print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (