    numerator1, denominator1 := strconv.Atoi(strings.Split(x, "/")[0]), strconv.Atoi(strings.Split(x, "/")[1])
    numerator2, denominator2 := strconv.Atoi(strings.Split(n, "/")[0]), strconv.Atoi(strings.Split(n, "/")[1])

    gcd := GCD(denominator1*denominator2, numerator1*numerator2)
    if gcd > 1 {
        numerator1 /= gcd
        numerator2 /= gcd
        denominator1 /= gcd
        denominator2 /= gcd
    }

    if numerator1 == denominator2 && numerator2 == denominator1 {
        return true
    }
    return false
}

func GCD(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}