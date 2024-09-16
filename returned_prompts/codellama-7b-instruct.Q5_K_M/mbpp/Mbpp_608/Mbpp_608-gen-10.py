"""
def bell_Number(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return sum(bell_Number(i) for i in range(n))
"""
