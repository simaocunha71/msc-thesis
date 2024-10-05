    x_num, _ := strconv.ParseInt(strings.Split(x, "/")[0], 10, 64)
    x_den, _ := strconv.ParseInt(strings.Split(x, "/")[1], 10, 64)
    n_num, _ := strconv.ParseInt(strings.Split(n, "/")[0], 10, 64)
    n_den, _ := strconv.ParseInt(strings.Split(n, "/")[1], 10, 64)

    x_num_n = x_num * n_den
    n_num_x = n_num * x_den

    return x_num_n == n_num_x
}