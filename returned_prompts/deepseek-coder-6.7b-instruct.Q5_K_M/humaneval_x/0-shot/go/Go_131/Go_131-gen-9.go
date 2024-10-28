    for i := 0; i < len(s); i++ {
        digit, _ := strconv.Atoi(string(s[i]))
        if digit%2 == 1 {
            product *= digit
        }
    }

    if product == 1 {
        return 0
    }

    return product
}


