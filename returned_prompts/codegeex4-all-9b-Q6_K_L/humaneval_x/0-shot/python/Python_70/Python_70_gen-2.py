def strange_sort_list(lst):
    if not lst:
        return lst
    lst.sort()
    res = []
    while lst:
        res.append(lst.pop(0))
        if lst:
            res.append(lst.pop())
    return res

print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))