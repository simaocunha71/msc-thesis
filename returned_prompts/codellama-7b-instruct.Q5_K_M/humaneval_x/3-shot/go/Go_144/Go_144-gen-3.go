    x_numerator, x_denominator, err := strconv.Atoi(strings.Split(x, "/")[0])
    if err != nil {
        return false
    }

    n_numerator, n_denominator, err := strconv.Atoi(strings.Split(n, "/")[0])
    if err != nil {
        return false
    }

    if x_numerator * n_denominator == n_numerator * x_denominator {
        return true
    } else {
        return false
    }
}



