    xn := strings.Split(x, "/")
    nn := strings.Split(n, "/")

    x_num, _ := strconv.Atoi(xn[0])
    x_denom, _ := strconv.Atoi(xn[1])
    n_num, _ := strconv.Atoi(nn[0])
    n_denom, _ := strconv.Atoi(nn[1])

    return (x_num * n_denom) == (n_num * x_denom)
}



