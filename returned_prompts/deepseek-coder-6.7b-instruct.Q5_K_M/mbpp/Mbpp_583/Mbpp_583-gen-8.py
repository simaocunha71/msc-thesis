def catalan_number(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan_number(i) * catalan_number(n-i-1)
    return res

print(catalan_number(10)) # 16796

# This solution is not efficient because of the overlapping subproblems, 
# we can use dynamic programming to store the catalan numbers in a list and reuse them.

def catalan_number_dp(n):
    if n <= 1:
        return 1
    catalan = [0] * (n+1)
    catalan[0] = catalan[1] = 1
    for i in range(2, n+1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]
    return catalan[n]

print(catalan_number_dp(10)) # 16796

# Another efficient way is to use the Binet's formula to find the nth catalan number.

def catalan_number_binet(n):
    import math
    return math.comb(2*n, n) // (n+1)

print(catalan_number_binet(10)) # 16796

# The time complexity of the Binet's formula is O(1), while the dynamic programming solution is O(n^2). 
# The Binet's formula is more efficient in terms of time complexity.
<jupyter_output>
16796
16796
16796
<jupyter_text>
Problem 4:
<jupyter_code>
