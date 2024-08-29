def pancake_sort(lst: list) -> list:
    n = len(lst)
    for i in range(n):
        max_idx = max_element(lst, 0, n-i)
        lst = flip(lst, max_idx)
        lst = flip(lst, n-i-1)
    return lst

def max_element(lst: list, start: int, end: int) -> int:
    max_idx = start
    for i in range(start, end):
        if lst[i] > lst[max_idx]:
            max_idx = i
    return max_idx

def flip(lst: list, end: int) -> list:
    start = 0
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst

print(pancake_sort([15, 79, 25, 38, 69]))

#output: [15, 25, 38, 69, 79]
<jupyter_output>
[15, 25, 38, 69, 79]
<jupyter_text>
Question 3:Write a Python function that will take two lists of equal length and return a list of the sums of the elements with the same indices from the two given lists. For example, if the two lists are [1, 2, 3] and [4, 5, 6], the function should return [5, 7, 9].
<jupyter_code>
def sum_lists(list1, list2):
    return [a + b for a, b in zip(list1, list2)]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(sum_lists(list1, list2))

#output: [5, 7, 9]
<jupyter_output>
[5, 7, 9