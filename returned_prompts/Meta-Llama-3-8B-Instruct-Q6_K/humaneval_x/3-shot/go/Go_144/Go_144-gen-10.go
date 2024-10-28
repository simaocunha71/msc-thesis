    x_num, _ := strconv.Atoi(strings.Split(x, "/")[0])
    x_denom, _ := strconv.Atoi(strings.Split(x, "/")[1])
    n_num, _ := strconv.Atoi(strings.Split(n, "/")[0])
    n_denom, _ := strconv.Atoi(strings.Split(n, "/")[1])

    x_result := float64(x_num) / float64(x_denom)
    n_result := float64(n_num) / float64(n_denom)

    return math.Mod(x_result*n_result, 1) == 0
}