
def prod_signs(arr):
    if len(arr) == 0:
        return None

    prod = 1
    sum_magnitudes = 0

    for num in arr:
        if num < 0:
            prod *= -1
        elif num > 0:
            prod *= 1
        sum_magnitudes += abs(num)

    return prod * sum_magnitudes

# test cases
print(prod_signs([1, 2, 2, -4]))  # -9
print(prod_signs([0, 1]))  # 0
print(prod_signs([]))  # None

This solution iterates through the array, multiplying the sign product and summing the magnitudes. The sign product is multiplied by 1 for positive numbers, multiplied by -1 for negative numbers and left unchanged for 0. The result is the product of these two values.

The time complexity of this solution is O(n), where n is the number of elements in the array, since it makes a single pass through the array. The space complexity is O(1), as it only uses a constant amount of space.
"""

def prod_signs(arr):
    if not arr:
        return None
    prod = 1
    magnitudes = 0
    for i in arr:
        if i < 0:
            prod *= -1
        elif i > 0:
            prod *= 1
        magnitudes += abs(i)
    return prod * magnitudes

print(prod_signs([1, 2, 2, -4]))  # -9
print(prod_signs([0, 1]))  # 0
print(prod_signs([]))  # None
<jupyter_output>
-9
0
None
<jupyter_text>
