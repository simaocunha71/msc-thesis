def next_Perfect_Square(n):
    num = (int)(n**0.5)
    if(num * num != n):
        num += 1
    while(num * num <= n):
        num += 1
    return num*num

def test_next_Perfect_Square():
    assert next_Perfect_Square(35) == 36
    print("All Tests Passed")

test_next_Perfect_Square()







"""
def next_Perfect_Square(n):
    sqrt_n = int(math.sqrt(n))
    while sqrt_n ** 2 != n:
        sqrt_n += 1
    return sqrt_n ** 2
"""


"""
def next_Perfect_Square(n):
    x = int(math.ceil(math.sqrt(n)))
    while x * x <= n:
        x += 1
    return x * x
"""


"""
import math

def next_Perfect_Square(n):
    sqrt_n = math.ceil(math.sqrt(n))
    while sqrt_n ** 2 != n:
        sqrt_n += 1
    return sqrt_n ** 2
"""


"""
def next_Perfect_Square(n):
    sqrt_n = int(math.sqrt(n))
    while sqrt_n ** 2 < n:
        sqrt_n += 1
    return sqrt_n ** 2
"""


"""
def next_Perfect_Square(n):
    sqrt_n = int(math.sqrt(n))
    while sqrt_n ** 2 != n:
        sqrt_n += 1
    return sqrt_n ** 2
"""


"""
def next_Perfect_Square(n):
    sqrt_n = int(n**0.5)
    while sqrt_n * sqrt_n <= n:
        sqrt_n += 1
    return sqrt_n * sqrt_n
"""


