
    if not arr:
        return None
    else:
        sum_magnitudes = 0
        product_signs = 1
        for num in arr:
            sum_magnitudes += abs(num)
            if num < 0:
                product_signs *= -1
            elif num > 0:
                product_signs *= 1
            else:
                return 0
        return sum_magnitudes * product_signs

print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))

"""
Output:
-9
0
None
"""

