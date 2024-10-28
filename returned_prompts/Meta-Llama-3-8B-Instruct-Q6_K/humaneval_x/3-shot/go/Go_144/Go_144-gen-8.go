    x_num, _ := strconv.Atoi(strings.Split(x, "/")[0])
    x_den, _ := strconv.Atoi(strings.Split(x, "/")[1])
    n_num, _ := strconv.Atoi(strings.Split(n, "/")[0])
    n_den, _ := strconv.Atoi(strings.Split(n, "/")[1])

    gcd := GCD(x_den*n_den, x_num*n_num)
    return x_den*n_den/gcd == x_num*n_num/gcd
}

func GCD(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}