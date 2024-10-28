    product := 1
    str := strconv.Itoa(n)

    for _, v := range str {
        digit, _ := strconv.Atoi(string(v))
        if digit % 2 != 0 {
            product *= digit
        }
    }
    return product
}



