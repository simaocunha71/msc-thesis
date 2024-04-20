"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""
from typing import List

def decimal_to_binary(n: int):
    ret = str(n)
    length = len(ret)  # the size of your binary string that you will return
    while (length < 8 and n > 0):  # while (your binary string is shorten to less than 4, continue to add more bits in binary form)
        length += 1
        if not n % 2:
            ret = str(n/2 + "1") + ret[::-1]
        else:
            ret = str(n/2 + "0") + ret[::-1]
    return ret

# Binary to Decimal
if __name__ == '__main__':
    print(decimal_to_binary(8))