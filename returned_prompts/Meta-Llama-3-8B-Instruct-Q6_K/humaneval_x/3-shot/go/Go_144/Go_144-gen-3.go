    xNum, _ := strconv.Atoi(strings.Split(x, "/")[0])
    xDen, _ := strconv.Atoi(strings.Split(x, "/")[1])
    nNum, _ := strconv.Atoi(strings.Split(n, "/")[0])
    nDen, _ := strconv.Atoi(strings.Split(n, "/")[1])

    gcd := GCD(xDen, nDen)
    newXNum := xNum * (nDen / gcd)
    newXDen := xDen / gcd

    return newXNum == nNum * (xDen / gcd)
}

func GCD(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}