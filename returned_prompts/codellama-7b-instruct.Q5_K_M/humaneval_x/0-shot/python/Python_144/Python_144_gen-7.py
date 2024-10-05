
def simplify(x, n):
    x, n = Fraction(x), Fraction(n)
    return (x * n).denominator == 1

def simplify(x, n):
    x, n = Fraction(x), Fraction(n)
    return x.numerator * n.denominator == n.numerator * x.denominator

def simplify(x, n):
    x, n = Fraction(x), Fraction(n)
    return x.denominator * n.denominator == x.numerator * n.numerator

def simplify(x, n):
    x, n = Fraction(x), Fraction(n)
    return x.denominator == n.denominator and x.numerator % n.numerator == 0

def simplify(x, n):
    x, n = Fraction(x), Fraction(n)
    return x.denominator == n.denominator and x.numerator // n.numerator == 1

def simplify(x, n):
    x, n = Fraction(x), Fraction(n)
    return x.denominator == n.denominator and x.numerator % n.numerator == 0 and x.numerator // n.numerator == 1

def simplify(x, n):
    x, n = Fraction(x), Fraction(n)
    return x.denominator == n.denominator and x.numerator % n.numerator == 0 and x.numerator // n.numerator == 1 and x.numerator * n.denominator == n.numerator * x.denominator

def simplify(x, n):
    x, n = Fraction(x), Fraction(n)
    return x.denominator == n.denominator and x.numerator % n.numerator == 0 and x.numerator // n.numerator == 1 and x.numerator * n.denominator == n.numerator * x.denominator and x.numerator == n.numerator

def simplify(x, n):
    x, n = Fraction(x), Fraction(