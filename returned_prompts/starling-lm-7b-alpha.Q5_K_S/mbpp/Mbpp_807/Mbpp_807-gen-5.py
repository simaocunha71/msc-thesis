def first_odd(lst):
    for num in lst:
        if num%2 != 0:
            return num

# Test
assert first_odd([1,3,5]) == 1

