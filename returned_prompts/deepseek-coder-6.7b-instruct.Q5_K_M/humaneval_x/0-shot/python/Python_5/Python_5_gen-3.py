from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))

"""
Output:
[]
[1, 4, 2, 4, 3]
"""

Explanation:
The function intersperse takes in a list of integers 'numbers' and an integer 'delimeter' as input. It first initializes an empty list 'result'. Then it iterates over 'numbers' with the help of a for loop. In the loop, it appends the current element to 'result', and if the current element is not the last one in 'numbers', it appends 'delimeter' to 'result'. Finally, it returns 'result' as the output.

This way, the 'delimeter' is inserted between every two consecutive elements of 'numbers' in the output list. If the input list 'numbers' is empty, the output list 'result' remains empty.
"""

"""
Solution:
The given function intersperse takes a list of integers 'numbers' and an integer 'delimeter' as input. It first initializes an empty list 'result'. Then it iterates over 'numbers' with the help of a for loop. In the loop, it appends the current element to 'result' and if the current element is not the last one in 'numbers', it appends 'delimeter' to 'result'. Finally, it returns 'result' as the output.

This way, the 'delimeter' is inserted between every two consecutive elements of 'numbers' in the output list. If the input list 'numbers' is empty, the output list 'result' remains empty.
"""

"""
Test Cases:

1. intersperse([], 4)
   Output: []
   Explanation: The input list is empty, so the output list is also empty.
