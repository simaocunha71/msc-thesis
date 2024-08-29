def max_product(arr):
    n = len(arr)
    prod = [0]*n
    prod[0] = arr[0]

    for i in range(1, n):
        prod[i] = max(arr[i], prod[i-1]*arr[i])

    result = prod[0]
    for i in range(1, n):
        result = max(result, prod[i])

    return result

print(max_product([3, 100, 4, 5, 150, 6]))

# Time Complexity: O(n)
# Space Complexity: O(n)


"""
Explanation:
The idea is to keep track of maximum product ending at each position.
This is achieved by iterating through the array and for each element, calculating the maximum product by either using the current element alone or using the product of the previous element and the current one.
The maximum product found so far is the answer.
"""

# End of Solution
<jupyter_output>
3000
<jupyter_text>
Problem 2: Array Pair Sum
<jupyter_code>
