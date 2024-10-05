    if a == 0 {
        return b
    }
    if b == 0 {
        return a
    }
    if a < b {
        return GreatestCommonDivisor(a, b%a)
    }
    return GreatestCommonDivisor(b, a%b)
}



