def next_smallest(lst):
    if len(lst) < 2 or len(set(lst)) < 2:
        return None
    smallest = min(lst)
    lst.remove(smallest)
    return min(lst)

print(next_smallest([1, 2, 3, 4, 5]))  # 2
print(next_smallest([5, 1, 4, 3, 2]))  # 2
print(next_smallest([]))  # None
print(next_smallest([1, 1]))  # None