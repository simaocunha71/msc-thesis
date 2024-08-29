def pancake_sort(lst: list) -> list:
    for i in range(len(lst), 0, -1):
        max_idx = lst[0:i].index(max(lst[0:i]))
        if max_idx != i - 1:
            lst[0:i] = lst[max_idx::-1] + lst[i:]
    return lst


print(pancake_sort([15, 79, 25, 38, 69]))

# or

def pancake_sort(lst: list) -> list:
    for i in range(len(lst), 0, -1):
        max_idx = lst.index(max(lst[:i]))
        if max_idx != i - 1:
            lst = lst[max_idx::-1] + lst[i:]
    return lst


print(pancake_sort([15, 79, 25, 38, 69]))

"""
Explanation:
Pancake sorting is a type of sorting algorithm that is performed on a stack. The idea is to sort the stack using the minimum number of pancake flips. 
The algorithm works by dividing the problem into smaller subproblems and solving them recursively. 

The pancake sorting algorithm consists of two steps:
1. Flip the elements of the array to the maximum element to the first.
2. Flip the maximum element to the first.

The algorithm continues this process until the array is sorted. 

The time complexity of the pancake sorting algorithm is O(n^2), where n is the number of elements in the array.
"""

# Another example

def pancake_sort(lst: list) -> list:
    for i in range(len(lst), 0, -1):
        max_idx = lst.index(max(lst[:i]))
        if max_idx != i - 1:
            lst = lst[max_idx::-1] + lst[i:]
