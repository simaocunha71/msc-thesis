    product := 1
    for n > 0 {
        digit := n % 10
        n = n / 10
        if digit%2 != 0 {
            product *= digit
        }
    }
    if product == 1 {
        return 0
    }
    return product
}

