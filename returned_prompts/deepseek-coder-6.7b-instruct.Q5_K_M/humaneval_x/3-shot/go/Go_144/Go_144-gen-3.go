    x_parts := strings.Split(x, "/")
    n_parts := strings.Split(n, "/")

    x_num, _ := strconv.Atoi(x_parts[0])
    x_denom, _ := strconv.Atoi(x_parts[1])
    n_num, _ := strconv.Atoi(n_parts[0])
    n_denom, _ := strconv.Atoi(n_parts[1])

    product_num := x_num * n_num
    product_denom := x_denom * n_denom

    return product_num % product_denom == 0
}



