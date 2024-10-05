func GreatestCommonDivisor(a int,b int) int{
    if b == 0 {
        return a
    }
    return GreatestCommonDivisor(b, a%b)
}