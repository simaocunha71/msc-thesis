"""
Here is a Python function that sets all even bits of a given number:

def even_bit_set_number(n):
    return n | (n << 1)

In this function, the bitwise OR (|) operator is used to set all even bits of the input number. The bitwise left shift (<<) operator is used to shift all even bits of the number to the left by one position. When we apply the bitwise OR operation between the original number and its left-shifted version, it sets all even bits of the number.

For example, if we call the function with the number 10, the function will return 10 itself because all even bits of 10 are already set.

Here's a sample usage of the function:

def test_even_bit_set_number():
    assert even_bit_set_number(10) == 10
    print("All tests passed.")

if __name__ == "__main__":
    test_even_bit_set_number()
"""

from __future__ import print_function
from __future__ import division
from future_builtins import *
import sys
import math
import os
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from cStringIO import StringIO
else:
    from io import BytesIO as StringIO


def even_bit_set_number(n):
    return n | (n << 1)


def main():
    n = int(input())
    print(even_bit_set_number(n))


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd