"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""

def even_bit_set_number(n):
    if n & (2^5 - 1) != 0:
        even_bit_set = 0xFFFFFF&n
        return even_bit_set
    else:
        return n

if __name__ == "__main__":
    assert even_bit_set_number(135472348) == (2^5 - 1)
