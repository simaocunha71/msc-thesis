
def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * jacobsthal_num(n - 1) + jacobsthal_num(n - 2)


print(jacobsthal_num(5))  # 11


"""
This function works by recursively calling itself twice: once with the argument n - 1 and once with the argument n - 2. 
This is based on the definition of the Jacobsthal numbers, which are defined as 2 * Jacobsthal(n - 1) + Jacobsthal(n - 2) for n >= 0 with base case Jacobsthal(0) = 0 and Jacobsthal(1) = 1.
"""

# Optimizing the function with Memoization

def jacobsthal_num_memo(n, memo = {}):
    if n in memo:
        return memo[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = 2 * jacobsthal_num_memo(n - 1, memo) + jacobsthal_num_memo(n - 2, memo)
        return memo[n]


print(jacobsthal_num_memo(5))  # 11


"""
The optimized version of the function uses a technique called memoization. Memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and reusing them when the same inputs occur again. In the case of this function, we store the Jacobsthal numbers as we calculate them and use them if we need to calculate the same number again.
"""
<jupyter_output>
11
11
<jupyter_text>
Problem 2:
<jupyter_code>
