    product := 1
    str := strconv.Itoa(n)

    for _, c := range str {
        digit, _ := strconv.Atoi(string(c))
        if digit % 2 != 0 {
            product *= digit
        }
    }

    return product
}



