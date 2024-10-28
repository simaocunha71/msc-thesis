    return ''.join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))


# Run tests
import doctest
if doctest.testmod().failed == 0:
    print("All tests passed.")
else:
    print("Some tests failed.")

# Created by FireFly 10/19/2020


```
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))
```