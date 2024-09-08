def add_lists(lst, tpl):
    return tpl + tuple(lst)

print(add_lists([5, 6, 7], (9, 10)))

# Output: (9, 10, 5, 6, 7)


