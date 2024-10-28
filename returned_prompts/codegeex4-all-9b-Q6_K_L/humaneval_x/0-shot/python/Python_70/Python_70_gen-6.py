def strange_sort_list(lst):
    res = []
    while len(lst):
        res.append(min(lst))
        lst.remove(min(lst))
        if len(lst):
            res.append(max(lst))
            lst.remove(max(lst))
    return res

print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))

# [1, 4, 2, 3]
# [5, 5, 5, 5]
# []
