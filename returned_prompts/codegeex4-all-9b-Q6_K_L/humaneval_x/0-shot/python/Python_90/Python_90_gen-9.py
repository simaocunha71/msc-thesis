def next_smallest(lst):
    if len(lst) < 2:
        return None
    unique_lst = list(set(lst))
    if len(unique_lst) < 2:
        return None
    unique_lst.sort()
    return unique_lst[1]

print(next_smallest([1, 2, 3, 4, 5])) # 2
print(next_smallest([5, 1, 4, 3, 2])) # 2
print(next_smallest([])) # None
print(next_smallest([1, 1])) # None