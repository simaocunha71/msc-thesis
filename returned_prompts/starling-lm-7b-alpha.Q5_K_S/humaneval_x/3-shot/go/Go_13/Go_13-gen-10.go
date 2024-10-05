    if a > b {
        return GreatestCommonDivisor(b,a)
    }
    if a == 0 {
        return b
    }
    return GreatestCommonDivisor(b%a, a)
}



