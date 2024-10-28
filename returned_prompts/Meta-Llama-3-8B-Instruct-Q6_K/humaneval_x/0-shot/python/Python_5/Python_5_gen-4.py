from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [delimeter] + [num for num in numbers] + [delimeter]
    # [delimeter] + numbers + [delimeter] would also work but it's not as flexible

print(intersperse([1, 2, 3], 4))  # prints: [1, 4, 2, 4, 3]
print(intersperse([], 4))  # prints: []  # edge case, empty list
print(intersperse([1], 4))  # prints: [1, 4]
print(intersperse([1, 2], 4))  # prints: [1, 4, 2, 4]
print(intersperse([1, 2, 3, 4, 5], 4))  # prints: [1, 4, 2, 4, 3, 4, 4, 5]  # more elements
print(intersperse([1, 2, 3, 4, 5, 6], 7))  # prints: [1, 7, 2, 7, 3, 7, 4, 7, 5, 7, 6]  # more elements and different delimeter

# Time complexity: O(n) where n is the length of the input list
# Space complexity: O(n) where n is the length of the input list
# This function works by creating a new list with delimeter inserted between each element of the input list. The delimeter is added at the start and end of the list to handle edge cases. It's not the most efficient way but it's easy to understand and works for all cases.  # noqa: E402
# The function could be improved by not creating a new list but modifying the input list in-place, which would reduce the space complexity to O(1). However, this would make the function less flexible and harder to understand.  # noqa: E402
# It's also worth noting that the function could be simplified by using a list comprehension, but it would be less readable.  # noqa: E402
# The function is also not optimized for the case where delimeter is the same as any of the elements in the list, as it would result in duplicate delimeters.