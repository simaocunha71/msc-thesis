from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join('1' if i != j else '0' for i, j in zip(a, b))
# or
    return ''.join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))
# or
    return ''.join(bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a)))  # Python 3.10+
# or
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result
# or
    result = ''
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result
# or
    return ''.join(map(str, [int(i) ^ int(j) for i, j in zip(a, b)]))  # Python 3.10+
# or
    return ''.join(str(int(a, 2) ^ int(b, 2)) for i in range(len(a)))
# or
    result = ''
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result
# or
    return ''.join(map(str, [int(i) ^ int(j) for i, j in zip(a, b)]))
# or
    return ''.join(map(str, [int(i) ^ int(j) for i, j in zip(a, b)]))
# or
    return ''.join(map(str, [int(i) ^ int(j) for i, j in zip(a, b)]))
# or
    return ''.join(map(str, [int(i) ^ int(j) for i, j in zip(a, b)]))
# or
    return ''.join(map(str, [int(i) ^ int(j) for i, j in zip(a, b)]))
# or
    return ''.join(map(str, [int(i) ^ int(j) for i, j in zip(a, b)]))
# or
    return ''.join(map(str, [int(i) ^ int(j) for i, j in zip(a, b)]))
# or
    return ''.join(map(str, [int(i) ^ int(j) for i, j in zip(a, b)]))
# or
   