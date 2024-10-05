    if b == 0 {
        return a
    }
    return GreatestCommonDivisor(b, a%b)
} // This function uses recursion to find the GCD of two numbers. It keeps dividing the larger number by the smaller number until the remainder is zero, at which point it returns the smaller number. This is the GCD because it is the largest number that divides both numbers without leaving a remainder.