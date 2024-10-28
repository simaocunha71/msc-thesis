def prod_signs(arr):
    if not arr: return None
    else:
        return sum(abs(x) * (1 if x > 0 else -1 if x < 0 else 0) for x in arr)

print(prod_signs([1, 2, 2, -4])) # -9
print(prod_signs([0, 1])) # 0
print(prod_signs([])) # None