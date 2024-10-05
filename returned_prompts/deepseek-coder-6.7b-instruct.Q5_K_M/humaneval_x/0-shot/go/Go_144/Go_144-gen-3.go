    // x * n = (xNumerator * nNumerator) / (xDenominator * nDenominator)
    // if x * n is a whole number then (xNumerator * nNumerator) should be divisible by (xDenominator * nDenominator)

    if (xNumerator * nNumerator) % (xDenominator * nDenominator) == 0 {
        return true
    }

    return false
}

The logic behind this is that the fraction simplification involves reducing the fraction to its lowest terms. That is, the numerator and the denominator should share no common factors except 1. If the numerator and the denominator can be divided by the same number (i.e., the gcd), then the fraction can be reduced.

If the fraction can be reduced to 1, then it evaluates to a whole number.

This function works by finding the greatest common divisor (gcd) of the numerators and the denominators of the fractions, and then checking if the numerator of the first fraction multiplied by the denominator of the second fraction is divisible by the denominator of the first fraction multiplied by the numerator of the second fraction. If it is, then the fraction can be simplified to 1 and evaluates to a whole number.

The function returns true if the fraction can be simplified to 1, and false otherwise.

This function assumes that the input fractions are valid, and that the denominators are not zero.

This function works by first splitting the input fractions into numerator and denominator parts, converting these parts to integers