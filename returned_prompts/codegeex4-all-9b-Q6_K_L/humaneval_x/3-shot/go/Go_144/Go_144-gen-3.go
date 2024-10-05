    x_num, _ := strconv.Atoi(strings.Split(x, "/")[0])
    x_denom, _ := strconv.Atoi(strings.Split(x, "/")[1])

    n_num, _ := strconv.Atoi(strings.Split(n, "/")[0])
    n_denom, _ := strconv.Atoi(strings.Split(n, "/")[1])

    if (x_num * n_denom) % (x_denom * n_num) == 0 {
        return true
    }else {
        return false
    }
}



