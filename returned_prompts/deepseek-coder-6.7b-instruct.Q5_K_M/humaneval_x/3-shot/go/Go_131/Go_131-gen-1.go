    str := strconv.Itoa(n)
    product := 1
    for _, c := range str {
        digit, _ := strconv.Atoi(string(c))
        if digit % 2 != 0 {
            product *= digit
        }
    }
    return product
}



