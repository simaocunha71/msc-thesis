from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert string to list of integers
    a = [int(x) for x in a]
    b = [int(x) for x in b]

    # pad shorter string with zeros
    if len(a) < len(b):
        a = [0] * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = [0] * (len(a) - len(b)) + b

    # perform XOR operation
    result = []
    for i in range(len(a)):
        result.append(str(a[i] ^ b[i]))

    # convert list of integers back to string
    result = ''.join(result)

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()