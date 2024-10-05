
    if len(arr) == 0:
        return None
    else:
        sum_magnitudes = 0
        prod_signs = 1
        for num in arr:
            sum_magnitudes += abs(num)
            if num < 0:
                prod_signs *= -1
            elif num > 0:
                prod_signs *= 1
            else:
                return 0
        return prod_signs * sum_magnitudes

print(prod_signs([1, 2, 2, -4])) # -9
print(prod_signs([0, 1])) # 0
print(prod_signs([])) # None


# 3.

