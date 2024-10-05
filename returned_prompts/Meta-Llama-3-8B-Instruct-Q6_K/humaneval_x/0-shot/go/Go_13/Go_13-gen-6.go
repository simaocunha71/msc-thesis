    if a < 0{
        a = -a
    }
    if b < 0{
        b = -b
    }
    if a == 0{
        return b
    }
    if b == 0{
        return a
    }
    remainder = a % b
    return GreatestCommonDivisor(b, remainder)

}
