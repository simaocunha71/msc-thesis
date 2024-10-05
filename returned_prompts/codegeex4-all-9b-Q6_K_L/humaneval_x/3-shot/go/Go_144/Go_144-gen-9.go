    x_num, _ := strconv.Atoi(strings.Split(x, "/")[0])
    x_den, _ := strconv.Atoi(strings.Split(x, "/")[1])

    n_num, _ := strconv.Atoi(strings.Split(n, "/")[0])
    n_den, _ := strconv.Atoi(strings.Split(n, "/")[1])

    return n_num % x_num == 0 && n_den % x_den == 0
}



