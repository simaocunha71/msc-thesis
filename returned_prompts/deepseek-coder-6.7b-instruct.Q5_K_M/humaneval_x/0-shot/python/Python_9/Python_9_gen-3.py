from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_num = numbers[0]
    result = []
    for num in numbers:
        if num > max_num:
            max_num = num
        result.append(max_num)
    return result

print(rolling_max([1, 2, 3, 2, 3, 4, 2]))

This will return the list: [1, 2, 3, 3, 3, 4, 4]
"""

from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    max_num = numbers[0]
    result = []
    for num in numbers:
        if num > max_num:
            max_num = num
        result.append(max_num)
    return result


print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # [1, 2, 3, 3, 3, 4, 4]

# The function works by looping through each number in the given list. If the current number is larger than the current maximum (`max_num`), 
# it updates `max_num` to the current number. Then, it appends the new maximum to the `result` list. At the end, `result` is returned, which contains 
# the maximum value found up to that point in the list for each element in the list.
<jupyter_output>
[1, 2, 3, 3, 3, 4, 4]
<jupyter_text>
1.2.4. Python Programming – Problem Solving and Programming Problems and Solutions – 36. Write a Python Program to find the sum of all the elements in a list using recursion.
<jupyter_code>
