"""
def pancake_sort(lst):
    for i in range(len(lst)):
        max_idx = max_element(lst, 0, len(lst) - i)
        lst = flip(lst, max_idx)
        lst = flip(lst, len(lst) - i - 1)
    return lst

def max_element(lst, start, end):
    max_idx = start
    for i in range(start, end):
        if lst[i] > lst[max_idx]:
            max_idx = i
    return max_idx

def flip(lst, end):
    start = 0
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst
"""

