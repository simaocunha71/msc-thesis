    if a==0||b==0{
        return 0
    }
    if a==b{
        return a
    }
    if a<b{
        return GreatestCommonDivisor(b,a)
    }
    return GreatestCommonDivisor(a%b,b)
}



