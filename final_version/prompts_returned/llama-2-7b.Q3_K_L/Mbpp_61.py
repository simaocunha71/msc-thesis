"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""
from typing import List, Tuple

def count_Substrings(number: int) -> int:
    """
    Recursive function to count total number of substrings with same sum of digits as their length.
    :param number: The input integer
    :return: the answer
    """
    
    # base case is when we have only one digit, so there can be only 1 substring that is its own length
    if number == 0 or int(number) == 1:
        return 1
    else:
        
        # else check for base cases
        count = 0
        length = len(str(int(number)))
        digit_sum = sum(map(lambda x: int(x), str(int(number))))
        if (digit_sum == len(str(int(number)))):
            count += 1
        
        # else recurse for different substrings and add them up at the end.
        return count + count_Substrings(digit_sum)