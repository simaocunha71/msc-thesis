
    if not arr:
        return None
    
    total = 0
    sign = 1
    
    for num in arr:
        if num < 0:
            sign *= -1
            total += abs(num)
        elif num > 0:
            sign *= 1
            total += num
        else:
            return 0
    
    return sign * total

# Test cases
print(prod_signs([1, 2, 2, -4]))  # -9
print(prod_signs([0, 1]))  # 0
print(prod_signs([]))  # None
print(prod_signs([-3, -4, 5]))  # 15
print(prod_signs([-3, 4, -5]))  # -15
print(prod_signs([3, 0, 4, -5]))  # 0

"""
The function "prod_signs" works by iterating over each number in the input list.
If the number is negative, the sign variable is multiplied by -1, and the absolute value of the number is added to the total.
If the number is positive, the sign variable is multiplied by 1 and the number is added to the total.
If the number is 0, the function immediately returns 0.
Finally, the sign variable is multiplied by the total and the result is returned.
"""

"""
The time complexity of the function is O(n), where n is the length of the input list, because it iterates over each number in the list once.
The space complexity is O(1), because the function only uses a constant amount of space to store the total and the sign variable.
"""
<jupyter_output>
-9
0
None
15
-15
0
<jupyter_text>
Question 2:
<jupyter_code>
