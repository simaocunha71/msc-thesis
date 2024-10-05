from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    counts = {}
    result = []
    for number in numbers:
        if number not in counts:
            counts[number] = 1
            result.append(number)
        else:
            counts[number] += 1
    return result

print(remove_duplicates([1, 2, 3, 2, 4]))

This solution works by using a dictionary to keep track of the counts of each number. When a number is encountered for the first time, it is appended to the result list and its count is incremented in the dictionary. If a number is encountered again, its count is incremented in the dictionary without appending it to the result list.
The complexity of this solution is O(n), where n is the length of the input list.
"""

# Q2:
"""
