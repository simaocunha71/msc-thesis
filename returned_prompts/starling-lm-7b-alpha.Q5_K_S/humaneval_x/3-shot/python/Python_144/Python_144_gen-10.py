    from typing import Tuple
    from fractions import Fraction

    def gcd(a: int, b: int) -> int:
        """
        Calculate greatest common divisor of two numbers.
        >>> gcd(3, 5)
        1
        """

        while b:
            a, b = b, a % b
        return a

    x_num, x_den = Fraction(x).numerator, Fraction(x).denominator
    n_num, n_den = Fraction(n).numerator, Fraction(n).denominator
    lcm = x_den * n_den // gcd(x_den, n_den)

    if (x_num * n_den) % lcm == 0 and (n_num * x_den) % lcm == 0:
        return True
    else:
        return False


