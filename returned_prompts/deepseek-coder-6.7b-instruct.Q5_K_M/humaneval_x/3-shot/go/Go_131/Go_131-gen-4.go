    product := 1
    for _, c := range strconv.Itoa(n) {
        digit, _ := strconv.Atoi(string(c))
        if digit % 2 != 0 {
            product *= digit
        }
    }
    return product
}



