    x_parts := strings.Split(x, "/")
    n_parts := strings.Split(n, "/")

    x_numerator, _ := strconv.Atoi(x_parts[0])
    x_denominator, _ := strconv.Atoi(x_parts[1])
    n_numerator, _ := strconv.Atoi(n_parts[0])
    n_denominator, _ := strconv.Atoi(n_parts[1])

    return (x_numerator * n_numerator) % (x_denominator * n_denominator) == 0
}



