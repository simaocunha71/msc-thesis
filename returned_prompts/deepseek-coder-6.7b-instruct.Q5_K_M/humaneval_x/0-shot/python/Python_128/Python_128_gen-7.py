
    if not arr:
        return None
    else:
        sign = 1
        sum_abs = 0
        for num in arr:
            if num < 0:
                sign *= -1
            elif num > 0:
                sign *= 1
            else:
                return 0
            sum_abs += abs(num)
        return sign * sum_abs

print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))

# Output: -9, 0, None

'''
Explanation:

For the first example,

The product of all signs is -1 (since there are an even number of negative numbers).
The sum of the absolute values is 9 (|1| + |2| + |2| + |4|).
So, the final result is -1 * 9 = -9.

For the second example,

There are no negative numbers, so the product of all signs is 1.
The sum of the absolute values is 1 (|1|).
So, the final result is 1 * 1 = 1.

For the third example,

Since the array is empty, the function returns None.
'''

'''
Time Complexity: O(n), where n is the length of the array. This is because we are iterating through the array once.
Space Complexity: O(1), constant space, as we are not using any additional space that scales with the input size.
'''
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2:
<jupyter_code>
