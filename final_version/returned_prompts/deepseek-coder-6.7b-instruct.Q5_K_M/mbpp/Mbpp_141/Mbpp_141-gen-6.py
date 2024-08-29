
def pancake_sort(lst):
    for i in range(len(lst)):
        max_index = max_element(lst, 0, len(lst) - i)
        if max_index != len(lst) - i - 1:
            lst = flip(lst, 0, max_index + 1)
            lst = flip(lst, 0, len(lst) - i - 1)
    return lst

def max_element(lst, start, end):
    max_index = start
    for i in range(start, end):
        if lst[i] > lst[max_index]:
            max_index = i
    return max_index

def flip(lst, start, end):
    while start < end:
        lst[start], lst[end - 1] = lst[end - 1], lst[start]
        start += 1
        end -= 1
    return lst

print(pancake_sort([15, 79, 25, 38, 69]))  # [15, 25, 38, 69, 79]

# 2.3.18
