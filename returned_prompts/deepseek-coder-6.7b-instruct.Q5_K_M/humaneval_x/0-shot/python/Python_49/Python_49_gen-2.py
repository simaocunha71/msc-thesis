

def modp(n: int, p: int):
    if n == 0:
        return 1
    else:
        return (2 ** n) % p


if __name__ == '__main__':
    import doctest
    doctest.testmod()


This solution works by checking if n is 0. If it is, it returns 1 (since 2^0 = 1 mod p for any p). If n is not 0, it calculates 2^n modulo p using the power function with the modulus argument.
"""


def modp(n: int, p: int):
    if n == 0:
        return 1
    else:
        return (2 ** n) % p


if __name__ == '__main__':
    import doctest
    doctest.testmod()


"""
This function uses the concept of modular arithmetic and the power function. In modular arithmetic, the remainder of the division of one number by another number is called the modulus. The modulus operation is represented by the symbol %.

The function modp(n, p) calculates 2^n modulo p. If n is 0, it returns 1 (since 2^0 = 1 mod p for any p). If n is not 0, it calculates 2^n modulo p using the power function with the modulus argument.

The power function (**) in python raises the first operand to the power of the second operand. The modulus operator (%) returns the remainder of the division of the first operand by the second operand.

In the end, we use the doctest module to test the function with the provided examples. The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions and verifies if they work exactly as shown.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2:
<jupyter_code>
"""
