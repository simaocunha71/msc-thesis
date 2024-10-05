def prod_signs(arr):
    if not arr:
        return None
    prod = 1
    for i in arr:
        if i < 0:
            prod *= -1
        elif i == 0:
            return 0
    return sum(arr) * prod

print(prod_signs([1, 2, 2, -4]))  # -9
print(prod_signs([0, 1]))  # 0
print(prod_signs([]))  # None