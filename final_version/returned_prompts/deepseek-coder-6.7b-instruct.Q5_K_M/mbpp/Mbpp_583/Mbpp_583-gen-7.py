def catalan_number(n):
    if n<=1:
        return 1
    res = 0
    for i in range(n):
        res += catalan_number(i) * catalan_number(n-i-1)
    return res

print(catalan_number(10))

#Time Complexity: O(n^2)
#Space Complexity: O(n)

#Dynamic Programming Approach
"""
