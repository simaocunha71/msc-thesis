def prod_signs(arr):
    if not arr:
        return None
    prod = 1
    sum = 0
    for x in arr:
        prod *= (1 if x > 0 else -1 if x < 0 else 0)
        sum += abs(x)
    return prod * sum

print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))