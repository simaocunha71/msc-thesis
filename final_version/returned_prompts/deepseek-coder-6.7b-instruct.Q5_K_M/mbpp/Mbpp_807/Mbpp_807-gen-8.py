def first_odd(lst):
    for i in lst:
        if i % 2 != 0:
            return i

print(first_odd([1,3,5])) # should return 1

