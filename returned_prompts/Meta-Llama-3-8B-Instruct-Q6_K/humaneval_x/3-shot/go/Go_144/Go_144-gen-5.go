    x_num, _ := strconv.Atoi(strings.Split(x, "/")[0])
    x_denom, _ := strconv.Atoi(strings.Split(x, "/")[1])
    n_num, _ := strconv.Atoi(strings.Split(n, "/")[0])
    n_denom, _ := strconv.Atoi(strings.Split(n, "/")[1])

    gcd := GCD(x_denom, n_denom)
    new_x_num := x_num * (n_denom / gcd)
    new_x_denom := x_denom / gcd

    return new_x_num == n_num * (x_denom / gcd)
}

func GCD(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}