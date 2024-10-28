    xNum, _ := strconv.Atoi(strings.Split(x, "/")[0])
    xDenom, _ := strconv.Atoi(strings.Split(x, "/")[1])
    nNum, _ := strconv.Atoi(strings.Split(n, "/")[0])
    nDenom, _ := strconv.Atoi(strings.Split(n, "/")[1])

    newNum := xNum * nDenom
    newDenom := xDenom * nNum

    gcd := func(a, b int) int {
        for b != 0 {
            a, b = b, a%b
        }
        return a
    }

    commonGCD := gcd(xDenom, nDenom)
    newNum /= commonGCD
    newDenom /= commonGCD

    return newNum == newDenom
}
}