    x_numerator, x_denominator, x_err := strconv.Atoi(strings.Split(x, "/")[0])
    x_denominator, x_err := strconv.Atoi(strings.Split(x, "/")[1])
    n_numerator, n_denominator, n_err := strconv.Atoi(strings.Split(n, "/")[0])
    n_denominator, n_err := strconv.Atoi(strings.Split(n, "/")[1])

    if x_err != nil || n_err != nil {
        return false
    }

    if x_denominator == 0 || n_denominator == 0 {
        return false
    }

    if x_denominator*n_denominator == x_numerator*n_numerator {
        return true
    }

    return false
}



