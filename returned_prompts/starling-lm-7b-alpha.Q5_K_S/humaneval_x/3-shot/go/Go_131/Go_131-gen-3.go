    product := 1
    is_odd := false
    for ; n > 0; n /= 10 {
        d := n % 10
        if d % 2 == 1 {
            if is_odd {
                product *= d
            } else {
                is_odd = true
                product = d
            }
        }
    }
    return product
}



