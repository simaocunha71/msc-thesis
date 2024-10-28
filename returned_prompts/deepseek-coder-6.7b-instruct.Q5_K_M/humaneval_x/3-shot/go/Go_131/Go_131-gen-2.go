    str := strconv.Itoa(n)
    product := 1
    for i := 0; i < len(str); i++ {
        digit, _ := strconv.Atoi(string(str[i]))
        if digit % 2 != 0 {
            product *= digit
        }
    }
    return product
}



