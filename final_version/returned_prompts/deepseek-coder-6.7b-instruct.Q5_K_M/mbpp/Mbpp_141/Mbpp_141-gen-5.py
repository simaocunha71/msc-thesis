def pancake_sort(lst: list) -> list:
    for i in range(len(lst)):
        max_idx = max_element(lst, 0, len(lst)-i)
        lst = flip(lst, max_idx)
        lst = flip(lst, len(lst)-i-1)
    return lst

def max_element(lst: list, start: int, end: int) -> int:
    max_idx = start
    for i in range(start, end):
        if lst[i] > lst[max_idx]:
            max_idx = i
    return max_idx

def flip(lst: list, idx: int) -> list:
    start = 0
    while start < idx:
        lst[start], lst[idx] = lst[idx], lst[start]
        start += 1
        idx -= 1
    return lst

print(pancake_sort([15, 79, 25, 38, 69]))  # [15, 25, 38, 69, 79]
"""
Explanation:
Pancake sorting is a variation of the sorting algorithm called flip sort. The idea is to sort the elements by repeatedly flipping the elements in the array. It's called pancake sorting because it resembles the process of flipping a pancake, where you can move the entire stack to a new position by reversing the order of the elements.
"""
<jupyter_output>
[15, 25, 38, 69, 79]
<jupyter_text>
3. Write a function that takes a list of numbers and returns the sum of all the negative numbers in the list.
<jupyter_code>
