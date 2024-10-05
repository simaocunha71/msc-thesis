    var x_numerator, x_denominator, n_numerator, n_denominator int
    var err error
    x_numbers := strings.Split(x, "/")
    n_numbers := strings.Split(n, "/")

    x_numerator, err = strconv.Atoi(x_numbers[0])
    if err != nil {
        return false
    }

    x_denominator, err = strconv.Atoi(x_numbers[1])
    if err != nil {
        return false
    }

    n_numerator, err = strconv.Atoi(n_numbers[0])
    if err != nil {
        return false
    }

    n_denominator, err = strconv.Atoi(n_numbers[1])
    if err != nil {
        return false
    }

    if x_numerator * n_denominator == n_numerator * x_denominator {
        return true
    } else {
        return false
    }
}



