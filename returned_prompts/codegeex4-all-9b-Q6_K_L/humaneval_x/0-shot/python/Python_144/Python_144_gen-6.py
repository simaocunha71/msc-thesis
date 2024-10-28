```python
def simplify(x, n):
    from fractions import Fraction
    frac = Fraction(x) * Fraction(n)
    return frac.denominator == 1

```
