    // To determine whether the result of x * n is a whole number,
    // we need to find the gcd of the numerator of x and the numerator of n,
    // and then check whether the denominator of x and the denominator of n is divisible by the gcd.
    var (
        xNumerator, nNumerator, xDenominator, nDenominator int
        gcd int
    )

    xNumerator, _ = strconv.Atoi(strings.Split(x, "/")[0])
    nNumerator, _ = strconv.Atoi(strings.Split(n, "/")[0])
    xDenominator, _ = strconv.Atoi(strings.Split(x, "/")[1])
    nDenominator, _ = strconv.Atoi(strings.Split(n, "/")[1])

    gcd = gcdOf(xNumerator, nNumerator)
    if gcd != 1 {
        return false
    }

    if xDenominator%gcd != 0 || nDenominator%gcd != 0 {
        return false
    }

    return true
}

func gcdOf(a, b int) int {
    if b == 0 {
        return a
    }

    return gcdOf(b, a%b)
}






















































































































































































