
def pancake_sort(lst):
    for i in range(len(lst)):
        max_index = max_element(lst, 0, i)
        lst = flip(lst, max_index)
        lst = flip(lst, i)
    return lst

def max_element(lst, start, end):
    max_index = start
    for i in range(start, end):
        if lst[i] > lst[max_index]:
            max_index = i
    return max_index

def flip(lst, k):
    start = 0
    while start < k:
        lst[start], lst[k] = lst[k], lst[start]
        start += 1
        k -= 1
    return lst

print(pancake_sort([15, 79, 25, 38, 69]))  # [15, 25, 38, 69, 79]
"""

