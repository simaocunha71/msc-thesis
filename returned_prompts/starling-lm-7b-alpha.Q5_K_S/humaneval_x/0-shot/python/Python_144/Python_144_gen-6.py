
from fractions import Fraction
from typing import Tuple

def simplify(x: str, n: str) -> bool:
    x_frac, n_frac = [Fraction(x), Fraction(n)]
    denominator = x_frac.numerator * n_frac.denominator
    numerator = x_frac.denominator * n_frac.numerator
    new_frac = Fraction(numerator, denominator)
    if new_frac.denominator == 1:
        return True
    return False


# Testing
print(simplify("1/5", "5/1"))  # True
print(simplify("1/6", "2/1"))  # False
print(simplify("7/10", "10/2"))  # False





# Some more test cases to consider
print(simplify("1/2", "2/3"))  # False
print(simplify("1/6", "3/2"))  # False
print(simplify("3/4", "4/6"))  # True
print(simplify("5/7", "7/8"))  # False
print(simplify("8/9", "9/10"))  # True
print(simplify("11/12", "12/13"))  # False
print(simplify("1/2", "3/1"))  # False




def simplify(x: str, n: str) -> bool:
    x_frac, n_frac = [Fraction(x), Fraction(n)]
    denominator = x_frac.numerator * n_frac.denominator
    numerator = x_frac.denominator * n_frac.numerator
    new_frac = Fraction(numerator, denominator)
    if new_frac.denominator == 1:
        return True
    return False



# Some more test cases to consider
print(simplify("1/2", "2/3"))  # False
print(simplify("1/6", "3/2"))  # False
print(simpl