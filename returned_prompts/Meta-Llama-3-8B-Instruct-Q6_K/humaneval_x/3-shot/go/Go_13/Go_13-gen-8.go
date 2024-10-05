    if b == 0 {
        return a
    }
    return GreatestCommonDivisor(b, a%b)
}  // This is an iterative solution. You can also use the Euclidean algorithm for a recursive solution.