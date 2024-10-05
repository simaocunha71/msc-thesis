    x_num, x_denom := strings.Split(x, "/")
    n_num, n_denom := strings.Split(n, "/")
    x_num_int, _ := strconv.Atoi(x_num)
    x_denom_int, _ := strconv.Atoi(x_denom)
    n_num_int, _ := strconv.Atoi(n_num)
    n_denom_int, _ := strconv.Atoi(n_denom)

    if (x_num_int * n_denom_int) % n_denom_int == 0 && (x_denom_int * n_num_int) % n_denom_int == 0 {
        return true
    } else {
        return false
    }
}



