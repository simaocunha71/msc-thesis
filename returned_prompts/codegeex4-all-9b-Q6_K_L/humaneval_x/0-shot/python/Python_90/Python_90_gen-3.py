def next_smallest(lst):
    if len(lst) < 2:
        return None
    lst.sort()
    for i in range(1, len(lst)):
        if lst[i] != lst[0]:
            return lst[i]
    return None

print(next_smallest([1, 2, 3, 4, 5])) # 2
print(next_smallest([5, 1, 4, 3, 2])) # 2
print(next_smallest([])) # None
print(next_smallest([1, 1])) # None