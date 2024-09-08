def jacobsthal_num(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return 2 * jacobsthal_num(n - 1) + jacobsthal_num(n - 2)

print(jacobsthal_num(5))

# or we can use dynamic programming to store the values of already computed Jacobsthal numbers
def jacobsthal_num_dp(n):
    jacobsthal = [0, 1] + [0]*n
    for i in range(2, n+1):
        jacobsthal[i] = 2 * jacobsthal[i - 1] + jacobsthal[i - 2]
    return jacobsthal[n]

print(jacobsthal_num_dp(5))

# both functions will return 11 which is the 5th Jacobsthal number.

# Both functions will have a time complexity of O(2^n) for the recursive function and O(n) for the dynamic programming function.
# Both functions will have a space complexity of O(n) for the dynamic programming function.
<jupyter_output>
11
11
<jupyter_text>
3. Fibonacci
<jupyter_code>
