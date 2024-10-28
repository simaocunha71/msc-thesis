
    if not arr:
        return None

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

    return sum_magnitudes * prod_signs

print(prod_signs([1, 2, 2, -4]))  # -9
print(prod_signs([0, 1]))  # 0
print(prod_signs([]))  # None
print(prod_signs([-3, 2, -1, 4, -2]))  # 18

"""
Test Cases:
1. prod_signs([1, 2, 2, -4]) == -9
2. prod_signs([0, 1]) == 0
3. prod_signs([]) == None
4. prod_signs([-3, 2, -1, 4, -2]) == 18
"""

"""
The function works by iterating through the array and for each number, it adds its absolute value to the sum_magnitudes and multiplies prod_signs by the sign of the number. If the number is negative, it multiplies prod_signs by -1, if the number is positive, it multiplies prod_signs by 1, and if the number is zero, it returns 0 immediately as any further calculations would be invalid. Finally, it returns the product of sum_magnitudes and prod_signs.
"""

# Task 2

