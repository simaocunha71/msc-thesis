```go
func Simplify(x, n string) bool {
    xNum, _ := strconv.Atoi(strings.Split(x, "/")[0])
    xDen, _ := strconv.Atoi(strings.Split(x, "/")[1])
    nNum, _ := strconv.Atoi(strings.Split(n, "/")[0])
    nDen, _ := strconv.Atoi(strings.Split(n, "/")[1])

    xMult, _ := strconv.Atoi(strings.Split(x, "/")[0])
    nMult, _ := strconv.Atoi(strings.Split(n, "/")[0])

    gcd := func(a, b int) int {
        for b != 0 {
            a, b = b, a%b
        }
        return a
    }

    xGcd := gcd(xNum, xDen)
    nGcd := gcd(nNum, nDen)

    xSimplifiedNum := xNum / xGcd
    xSimplifiedDen := xDen / xGcd

    nSimplifiedNum := nNum / nGcd
    nSimplifiedDen := nDen / nGcd

    xMult := xSimplifiedNum * nSimplifiedNum
    xDiv := xSimplifiedDen * nSimplifiedDen

    gcdResult := gcd(xMult, xDiv)

    xMult = xMult / gcdResult
    xDiv = xDiv / gcdResult

    return xMult == xDiv
}
```



This code first parses the input strings into their numerator and denominator values. Then, it calculates the greatest common divisor (GCD) of the numerator and denominator for each fraction, and simplifies the fractions by dividing both the numerator and denominator by the GCD. It then multiplies the numerator and denominator of the two simplified fractions together, and calculates the GCD of the resulting numerator and denominator. Finally, it checks if the resulting numerator is equal to the denominator, which means that the original product of the two fractions is a whole number. If it is, the function returns true; otherwise, it returns false.