    x_numerator, x_denominator := strings.Split(x, "/")
    n_numerator, n_denominator := strings.Split(n, "/")

    x_numerator_i, _ := strconv.Atoi(x_numerator)
    n_numerator_i, _ := strconv.Atoi(n_numerator)
    x_denominator_i, _ := strconv.Atoi(x_denominator)
    n_denominator_i, _ := strconv.Atoi(n_denominator)

    x_result := x_numerator_i * n_denominator_i
    n_result := n_numerator_i * x_denominator_i

    if x_result == n_result {
        return true
    }

    return false
}



