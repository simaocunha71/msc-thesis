    xn := strings.Split(x, "/")
    nn := strings.Split(n, "/")

    xNumerator, _ := strconv.Atoi(xn[0])
    xDenominator, _ := strconv.Atoi(xn[1])
    nNumerator, _ := strconv.Atoi(nn[0])
    nDenominator, _ := strconv.Atoi(nn[1])

    return (xNumerator * nDenominator) == (nNumerator * xDenominator)
}



