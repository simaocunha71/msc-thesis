def prod_signs(arr):
    if not arr:
        return None
    sign_prod = 1
    magnitude_sum = 0
    for num in arr:
        sign_prod *= (1 if num >= 0 else -1)
        magnitude_sum += abs(num)
    return sign_prod * magnitude_sum

print(prod_signs([1, 2, 2, -4]))  # -9
print(prod_signs([0, 1]))  # 0
print(prod_signs([]))  # None