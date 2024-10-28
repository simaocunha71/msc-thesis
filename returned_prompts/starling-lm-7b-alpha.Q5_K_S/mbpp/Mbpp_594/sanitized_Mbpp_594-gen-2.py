from typing import List
def diff_even_odd(nums: List[int]) -> int:
    evens = [num for num in nums if num % 2 == 0]
    odds = [num for num in nums if num % 2 == 1]
    return evens[0] - odds[0] if evens and odds else 0