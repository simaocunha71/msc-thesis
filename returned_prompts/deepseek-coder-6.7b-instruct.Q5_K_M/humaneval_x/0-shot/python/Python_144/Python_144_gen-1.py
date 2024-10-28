
    from fractions import Fraction

    def simplify(x, n):
        f1 = Fraction(x)
        f2 = Fraction(n)
        return (f1 * f2).denominator == 1

print(simplify("1/5", "5/1")) # True
print(simplify("1/6", "2/1")) # False
print(simplify("7/10", "10/2")) # False
"""

from fractions import Fraction

def simplify(x, n):
    f1 = Fraction(x)
    f2 = Fraction(n)
    return (f1 * f2).denominator == 1

print(simplify("1/5", "5/1")) # True
print(simplify("1/6", "2/1")) # False
print(simplify("7/10", "10/2")) # False
"""
"""
The function Fraction(x) transforms the string representation of a fraction into a fraction object.
The function (f1 * f2).denominator == 1 checks if the product of f1 and f2 is a whole number.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
**Task 5:** **Write a Python code that takes a string as input and returns the number of digits in the string.**
<jupyter_code>
"""
