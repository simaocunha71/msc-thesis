    product := 1
    is_all_even := true
    for n > 0 {
        d := n % 10
        if d % 2 == 1 {
            product *= d
            is_all_even = false
        }
        n /= 10
    }
    if is_all_even {
        return 0
    }
    return product
}



