    if b == 0 {
        return a
    } else {
        return GreatestCommonDivisor(b, a%b)
    }
}  // recursive version
// or
func GreatestCommonDivisor(a int, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}  // iterative version
}  // both versions return the GCD of a and b. The iterative version is more efficient.