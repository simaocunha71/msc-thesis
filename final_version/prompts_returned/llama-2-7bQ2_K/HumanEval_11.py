from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if not (len(a) == len(b)):
        raise ValueError("Lengh of two strings must be equal")
    n = 0
    r = ""
    for i, c in enumerate(a):
        if c == '1':
            n += 2 ** i
        else:
            n -= 2 ** i
        r += f'{n:0{len(str(n))}b}'
    return r[1:] + "0" * (len(r) - len("10"))
