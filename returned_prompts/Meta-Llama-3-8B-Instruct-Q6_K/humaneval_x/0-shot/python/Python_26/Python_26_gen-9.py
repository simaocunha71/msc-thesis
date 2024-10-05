from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
# Explanation: The function iterates over the input list, keeping track of the elements it has seen in a set. If an element is not in the set, it is added to the result list and to the set. This ensures that all elements are unique and the order is preserved. 
# Note: The time complexity is O(n), where n is the length of the input list, because we iterate over the list once. The space complexity is O(n), because in the worst case (when all elements are unique), the set will contain n elements. 
# Also, the function preserves the order of elements. This is achieved by iterating over the input list and adding elements to the result list in the same order. 
# The function can be used to remove duplicates from a list of integers while preserving the order. 
# It can be used in situations where the order of elements matters, such as in data processing or scientific computing. 
# It can also be used in situations where the number of unique elements is small compared to the total number of elements, such as in data compression or data deduplication.  # Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
# Explanation: The function iterates over the input list, keeping track of the elements it has seen in a set. If an element is not in the set, it is added to the result list and to the set. This ensures that all elements are unique and the order is preserved. 
# Note: The time complexity is O(n), where n is the length of the input list, because we iterate over the list once. The space complexity is O(n), because in the worst case (when all elements are unique), the set will contain n elements. 
# Also, the function preserves the order of elements. This is achieved by iterating over the input list and adding elements to the result list in the same order. 
# The function can be used to