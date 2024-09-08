"""
def left_rotate(n, d):
    return (n << d)|(n >> (32 - d))

print(left_rotate(16,2))
"""

assert left_rotate(16,2) == 64

