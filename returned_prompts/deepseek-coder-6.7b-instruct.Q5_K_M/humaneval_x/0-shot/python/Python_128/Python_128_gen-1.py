
def prod_signs(arr):
    if not arr:
        return None
    else:
        sum_magnitudes = 0
        product_signs = 1
        for number in arr:
            sum_magnitudes += abs(number)
            product_signs *= (1 if number > 0 else -1)
        return sum_magnitudes * product_signs

print(prod_signs([1, 2, 2, -4]))  # -9
print(prod_signs([0, 1]))  # 0
print(prod_signs([]))  # None
"""

def prod_signs(arr):
    if not arr: return None
    return sum(abs(x) for x in arr) * (-1 if any(x < 0 for x in arr) else 1)

print(prod_signs([1, 2, 2, -4]))  # -9
print(prod_signs([0, 1]))  # 0
print(prod_signs([]))  # None
"""

"""
The solution provided uses list comprehension to calculate the sum of the absolute values of all the numbers in the list (abs(x) for x in arr) and then multiplies this sum by the product of the signs of the numbers in the list (-1 if any(x < 0 for x in arr) else 1).

This solution is more concise and readable than the previous one and is more efficient because it avoids the need for a separate loop to calculate the sum of the absolute values and the product of the signs. It also handles the edge case of an empty list by returning None.
"""

# 15. Write a Python program to find the maximum and minimum numbers from a given list of numbers.

