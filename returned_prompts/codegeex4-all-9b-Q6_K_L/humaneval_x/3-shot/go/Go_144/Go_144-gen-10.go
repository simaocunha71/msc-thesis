    x_arr := strings.Split(x,"/")
    n_arr := strings.Split(n,"/")

    x_num,_ := strconv.Atoi(x_arr[0])
    x_den,_ := strconv.Atoi(x_arr[1])

    n_num,_ := strconv.Atoi(n_arr[0])
    n_den,_ := strconv.Atoi(n_arr[1])

    return (x_num*n_den)%x_den == 0
}

