"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""

def catalan_number(n):
    if not 2 < n < 4:
        return ""
    res = -1
    for i in range(3, n+1, 2):
        cnt = 0
        for j in range(i-1,-1,-2):
            p = (j + i) // 2
            if (p >= j and j>=4):
                cnt += (p - j )//(j+1)*(p-3)/(j+1)+(i-p+j-1)/(j+1)
    res = cnt * n
    return res
