def max_product(arr):
    if len(arr)==0:
        return 0
    max_prod = [0]*len(arr)
    max_prod[0] = arr[0]
    for i in range(1, len(arr)):
        max_prod[i] = max(arr[i], max_prod[i-1]*arr[i])
    return max(max_prod)

print(max_product([3, 100, 4, 5, 150, 6]))

# In this code, max_prod[i] stores the maximum product that can be obtained by multiplying numbers of an increasing subsequence of arr[0...i]. 
# The maximum product is obtained by either extending the previous maximum product by arr[i] if arr[i] is positive or by arr[i] itself if arr[i] is negative. 
# The final result is the maximum value in max_prod array.

# Time complexity: O(n) where n is the length of the input list. We traverse the list once to calculate max_prod.
# Space complexity: O(n) where n is the length of the input list. We use a list to store the maximum product for each index in the list.
<jupyter_output>
3000
<jupyter_text>
10. Write a Python function to find the minimum number of coins that you need to make up a certain amount. You can use any coin denomination available.
<jupyter_code>
def min_coins(coins, amount):
    MAX = float('inf')
    dp = [0] + [MAX] * amount

    for i in range(1, amount + 1):
        dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

    return dp[amount] if dp[amount] != MAX else -1

# Test the function
coins = [1, 2, 5]
amount = 11
print(min_coins(coins, amount))  # Output: 3
<jupyter_output>
3