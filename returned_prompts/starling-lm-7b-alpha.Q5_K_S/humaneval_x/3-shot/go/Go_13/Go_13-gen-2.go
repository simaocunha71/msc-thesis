    if a < b {
        return GreatestCommonDivisor(b, a)
    }
    if b == 0 {
        return a
    }
    if a%b == 0 {
        return b
    }
    return GreatestCommonDivisor(b, a%b)
}



