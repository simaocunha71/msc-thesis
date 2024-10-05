    if a == 0:
        return b
    if b == 0:
        return a
    return GreatestCommonDivisor(b%a,a)

}

