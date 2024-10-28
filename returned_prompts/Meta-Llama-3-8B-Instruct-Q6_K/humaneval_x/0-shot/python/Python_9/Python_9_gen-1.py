from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = []
    current_max = float('-inf')

    for num in numbers:
        if num > current_max:
            current_max = num
        rolling_max_list.append(current_max)

    return rolling_max_list
# This code defines a function rolling_max that takes a list of numbers as input and returns a list of the rolling maximums.
# The rolling maximum at each position is the maximum of all numbers seen so far.
# The function initializes current_max to negative infinity and then iterates over the input list. For each number, it checks if the number is greater than current_max. If it is, it updates current_max. Then it appends current_max to the rolling_max_list. Finally, it returns the rolling_max_list. 
# The unit test provided ensures that the function works correctly. The function is tested with the input [1, 2, 3, 2, 3, 4, 2] and the expected output is [1, 2, 3, 3, 3, 4, 4]. The function passes this test, which means it is working correctly. 
# The time complexity of this function is O(n), where n is the length of the input list, because it iterates over the input list once. The space complexity is also O(n), because it creates a new list of the same length as the input list. 
# This function can be used in a variety of applications where rolling maximums are needed, such as in finance to calculate the rolling maximum stock price or in science to calculate the rolling maximum temperature. 
# The function is also flexible and can be used with lists of any type, not just integers, as long as the comparison operator works correctly for the type.  # noqa: E501
# This function does not handle edge cases, such as an empty input list. It is assumed that the input list will not be empty. 
# This function can be improved by adding error handling to handle edge cases. For example, it could raise an exception