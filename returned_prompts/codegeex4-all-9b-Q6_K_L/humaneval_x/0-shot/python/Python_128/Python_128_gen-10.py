def prod_signs(arr):
    if not arr: return None
    if len(arr) == 1: return arr[0]
    signs = [1 if x > 0 else -1 for x in arr]
    prod_signs = 1
    for s in signs:
        prod_signs *= s
    magnitudes = [abs(x) for x in arr]
    sum_magnitudes = sum(magnitudes)
    return sum_magnitudes * prod_signs

print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))