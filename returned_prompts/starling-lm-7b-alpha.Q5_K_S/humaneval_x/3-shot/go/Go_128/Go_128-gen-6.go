    if len(arr) == 0 {
        return nil
    }

    product := 1
    for _, a := range arr {
        if a < 0 {
            product *= -1
        } else if a > 0 {
            product *= a
        } else {
            product = 0
        }
    }

    return -product
}



