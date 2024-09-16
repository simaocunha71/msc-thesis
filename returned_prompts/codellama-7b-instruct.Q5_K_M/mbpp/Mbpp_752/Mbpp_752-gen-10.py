"""
def jacobsthal_num(n):
    if n <= 0:
        return 0
    return sum(jacobsthal_num(n-i) for i in range(1, n+1))
"""
