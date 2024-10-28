    str_n := strconv.Itoa(n)
    product := 1
    for i := 0; i < len(str_n); i++ {
        digit, _ := strconv.Atoi(string(str_n[i]))
        if digit % 2 != 0 {
            product *= digit
        }
    }
    return product
}



