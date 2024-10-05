def add(lst):
    return sum(i for idx, i in enumerate(lst) if idx % 2 == 1 and i % 2 == 0)

print(add([4, 2, 6, 7])) #==> 2