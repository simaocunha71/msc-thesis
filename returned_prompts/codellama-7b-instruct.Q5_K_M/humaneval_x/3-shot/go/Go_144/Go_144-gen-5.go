    x_numerator, _ := strconv.Atoi(strings.Split(x, "/")[0])
    x_denominator, _ := strconv.Atoi(strings.Split(x, "/")[1])

    n_numerator, _ := strconv.Atoi(strings.Split(n, "/")[0])
    n_denominator, _ := strconv.Atoi(strings.Split(n, "/")[1])

    if x_numerator * n_denominator == x_denominator * n_numerator{
        return true
    }
    return false
}



