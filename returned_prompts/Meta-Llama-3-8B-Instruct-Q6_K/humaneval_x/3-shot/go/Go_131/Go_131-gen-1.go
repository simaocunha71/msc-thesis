    var product int
    for n > 0 {
        digit := n % 10
        if digit % 2 != 0 {
            product *= digit
        }
        n /= 10
    }
    if product == 0 {
        return 1
    }
    return product
}