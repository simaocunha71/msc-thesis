    product := 1
    for n > 0 {
        d := n % 10
        if d % 2 != 0 {
            product *= d
        }
        n /= 10
    }
    return product
}



