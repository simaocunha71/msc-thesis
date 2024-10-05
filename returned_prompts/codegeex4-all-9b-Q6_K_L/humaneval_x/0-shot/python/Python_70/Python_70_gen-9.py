def strange_sort_list(lst):
    if not lst:
        return []
    return [min(lst)] + strange_sort_list([i for i in lst if i > min(lst)])

print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))