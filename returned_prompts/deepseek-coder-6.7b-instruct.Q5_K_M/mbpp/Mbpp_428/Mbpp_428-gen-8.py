def shell_sort(lst):
    gap = len(lst) // 2
    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst

print(shell_shell([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]))
"""
Output:
[2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
"""

Explanation:
The shell sort function starts by defining the initial gap as half the length of the input list. For each gap value, it sorts the list by comparing elements that are gap positions apart, then reducing the gap by half until it becomes zero.
"""


# Test Case:

assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
assert shell_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]
assert shell_sort([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
assert shell_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert shell_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert shell_sort([1]) == [1]
assert shell_sort([]) == []

