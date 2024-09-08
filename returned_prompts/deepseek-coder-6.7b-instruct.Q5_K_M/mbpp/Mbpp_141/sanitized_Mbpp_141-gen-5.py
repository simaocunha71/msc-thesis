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