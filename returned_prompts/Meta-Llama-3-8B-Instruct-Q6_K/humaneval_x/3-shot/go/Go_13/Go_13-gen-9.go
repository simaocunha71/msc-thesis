    if b == 0 {
        return a
    }
    return GreatestCommonDivisor(b, a%b)
}
// This function uses recursion to calculate the GCD. It keeps dividing the larger number by the smaller number until the remainder is 0. The last non-zero remainder is the GCD. This is the Euclidean algorithm.