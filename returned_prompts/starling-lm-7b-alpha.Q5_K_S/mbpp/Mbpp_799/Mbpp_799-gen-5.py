"""
def left_rotate(number, d):
    bit_list = [0]*32
    for i in range(32):
        bit_list[i] = number & 1
        number >>= 1
    for i in range(d):
        bit_list.insert(0, bit_list.pop())
    return int(''.join(map(str, bit_list)), 2)
"""

def left_rotate(number, d):
    return (number << d) | (number >> (32 - d))


assert left_rotate(16,2) == 64
print(left_rotate(16,2))
"""
"""

def left_rotate(number, d):
    return (number << d) | (number >> (32 - d))
assert left_rotate(16,2) == 64
print(left_rotate(16,2))
"""

def left_rotate(number, d):
    return (number << d) | (number >> (32 - d))
assert left_rotate(16,2) == 64
print(left_rotate(16,2))


"""
def left_rotate(number, d):
    #return (number << d) | (number >> (32 - d))
    temp = number
    for i in range(d):
        temp <<= 1
        temp |= (temp >> 32)
    return temp

assert left_rotate(16,2) == 64
print(left_rotate(16,2))
"""

def left_rotate(number, d):
    return (number << d) | (number >> (32 - d))
assert left_rotate(16,2) == 64
print(left_rotate(16,2))


"""
def left_rotate(number, d):
    return (number << d) | (number >> (32 - d))

assert left_rotate(16,2) == 64
print(left_rotate(16,2))
"""

def left_rotate(number, d):
    return (number << d) | (