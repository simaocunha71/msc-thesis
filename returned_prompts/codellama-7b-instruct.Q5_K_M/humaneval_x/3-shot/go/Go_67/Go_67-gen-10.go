    var (
        num_of_apples,num_of_oranges,num_of_mango int
        err error
    )
    strs := strings.Split(s, " ")
    num_of_apples, err = strconv.Atoi(strs[0])
    num_of_oranges, err = strconv.Atoi(strs[1])
    num_of_mango = n - num_of_apples - num_of_oranges
    return num_of_mango
}



