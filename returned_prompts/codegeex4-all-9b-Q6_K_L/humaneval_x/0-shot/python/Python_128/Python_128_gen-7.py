def prod_signs(arr):
    if not arr:
        return None
    res = 1
    for i in arr:
        if i > 0:
            res *= 1
        elif i < 0:
            res *= -1
        else:
            res *= 0
    return res

print prod_signs([1, 2, 2, -4]) == -9
print prod_signs([0, 1]) == 0
print prod_signs([]) == None
print prod_signs([1, 2, 2, 4]) == 16