    var numerator1, numerator2, denominator1, denominator2 int
    var ok bool

    numerator1, ok = strconv.Atoi(strings.Split(x, "/")[0])
    if !ok {
        return false
    }
    denominator1, ok = strconv.Atoi(strings.Split(x, "/")[1])
    if !ok {
        return false
    }
    numerator2, ok = strconv.Atoi(strings.Split(n, "/")[0])
    if !ok {
        return false
    }
    denominator2, ok = strconv.Atoi(strings.Split(n, "/")[1])
    if !ok {
        return false
    }

    var gcd int = func(a, b int) int {
        if b == 0 {
            return a
        }
        return gcd(b, a%b)
    }(numerator1*denominator2, denominator1*numerator2)

    return numerator1*denominator2%gcd == 0 && denominator1*numerator2%gcd == 0
}



