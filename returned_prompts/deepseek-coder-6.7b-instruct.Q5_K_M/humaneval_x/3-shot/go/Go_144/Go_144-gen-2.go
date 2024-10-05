    x_parts := strings.Split(x, "/")
    n_parts := strings.Split(n, "/")

    x_num, _ := strconv.Atoi(x_parts[0])
    x_denom, _ := strconv.Atoi(x_parts[1])
    n_num, _ := strconv.Atoi(n_parts[0])
    n_denom, _ := strconv.Atoi(n_parts[1])

    return (x_num * n_denom) == (n_num * x_denom)
}



