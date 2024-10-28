    xNum, _ := strconv.Atoi(strings.Split(x, "/")[0])
    xDen, _ := strconv.Atoi(strings.Split(x, "/")[1])
    nNum, _ := strconv.Atoi(strings.Split(n, "/")[0])
    nDen, _ := strconv.Atoi(strings.Split(n, "/")[1])

    gcd := func(a, b int) int {
        for b != 0 {
            a, b = b, a%b
        }
        return a
    }

    xNum *= nDen
    nNum *= xDen
    gcdNum := gcd(xNum, nNum)

    return xNum/gcdNum == nNum/gcdNum
}