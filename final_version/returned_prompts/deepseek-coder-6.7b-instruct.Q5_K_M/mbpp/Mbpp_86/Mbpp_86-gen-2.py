"""
The nth centered hexagonal number can be calculated using the formula:
n(5n-3)/2.
"""

def centered_hexagonal_number(n):
    return n*(5*n-3)//2

print(centered_hexagonal_number(10)) # 271

# 2022-03-17 Thursday
# 