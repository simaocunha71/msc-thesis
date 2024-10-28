"""
def is_num_decagonal(n):
    return n * (n + 1) // 2 == 3

def decagonal_num(n):
    return n * (n + 1) // 2

def next_decagonal_num(num):
    return decagonal_num(num + 1)

assert is_num_decagonal(3) == 27
assert next_decagonal_num(27) == 45
"""
