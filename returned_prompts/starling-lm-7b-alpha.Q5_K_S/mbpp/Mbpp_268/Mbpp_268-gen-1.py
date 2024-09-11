"""
def find_star_num(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * (n - i + 1) * 2
    return sum

print(find_star_num(3))
"""

