    x_numerator := 0
    x_denominator := 0
    n_numerator := 0
    n_denominator := 0

    parts := strings.Split(x, "/")
    x_numerator, _ = strconv.Atoi(parts[0])
    x_denominator, _ = strconv.Atoi(parts[1])

    parts = strings.Split(n, "/")
    n_numerator, _ = strconv.Atoi(parts[0])
    n_denominator, _ = strconv.Atoi(parts[1])

    if x_numerator * n_denominator == x_denominator * n_numerator {
        return true
    }
    return false
}