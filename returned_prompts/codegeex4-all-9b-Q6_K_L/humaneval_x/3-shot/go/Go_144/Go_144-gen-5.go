    x_split := strings.Split(x, "/")
    n_split := strings.Split(n, "/")
    x_num, _ := strconv.Atoi(x_split[0])
    x_den, _ := strconv.Atoi(x_split[1])
    n_num, _ := strconv.Atoi(n_split[0])
    n_den, _ := strconv.Atoi(n_split[1])
    if x_num*n_den == x_den*n_num {
        return true
    }
    return false
}



