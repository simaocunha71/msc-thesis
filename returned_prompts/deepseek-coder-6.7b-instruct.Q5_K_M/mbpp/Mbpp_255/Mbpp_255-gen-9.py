
def combinations_colors(lst, n):
    import itertools
    return list(itertools.product(*([lst]*n)))

print(combinations_colors(["Red","Green","Blue"],1)) # [('Red',), ('Green',), ('Blue',)]


