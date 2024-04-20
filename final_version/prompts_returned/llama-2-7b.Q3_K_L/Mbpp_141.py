"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""
from typing import List

def pancake_sort(arr: List[int]) -> None:
    pancake_list = []
    for i in arr:
        if not isinstance(pancake_list[-1], int):
            pancake_list.append(-1)
        else:
            pancake_list.append(i)
    pancake_sort_nums = pancake_list[::-1]  # Sorting Numbers Reversed
    for i in range(len(pancake_list)):  # Putting Pancake Back Together
        if isinstance(pancake_list[i], int):  # Inserting Int Values Back into List
            pancake_sort_nums[i] = pancake_list[i]
    for i in range(len(pancake_list)):  # Sorting Int Values Back to Front
        if isinstance(pancake_sort_nums[i], int):
            pancake_sort_nums[i] = -1
        else:  # Resetting Pancake to Front of List
            pancake_sort_nums[i] = i+1
    print(pancake_sort_nums)