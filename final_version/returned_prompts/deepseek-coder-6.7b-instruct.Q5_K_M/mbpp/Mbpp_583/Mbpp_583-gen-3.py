def catalan_number(n):
    if n<=1:
        return 1
    res=0
    for i in range(n):
        res+=catalan_number(i)*catalan_number(n-i-1)
    return res

print(catalan_number(10)) #16796

# Note: This solution is not efficient for large numbers. It uses recursive approach and calculates the catalan number for each number from 0 to n. So, for large numbers it will take a lot of time.

# Using dynamic programming:
def catalan_number(n):
    if n<=1:
        return 1
    catalan = [0 for _ in range(n+1)]
    catalan[0] = 1
    catalan[1] = 1
    for i in range(2,n+1):
        for j in range(i):
            catalan[i] += catalan[j]*catalan[i-j-1]
    return catalan[n]

print(catalan_number(10)) #16796

# This is more efficient for large numbers. It uses the same recursive formula but stores the result of each calculation in a list so that it doesn't need to calculate it again.
<jupyter_output>
16796
16796
<jupyter_text>
**Question 2**
<jupyter_code>
