    result := 1
    is_odd := false

    for n > 0 {
        digit := n % 10
        if digit % 2 != 0 {
            is_odd = true
            result *= digit
        }
        n /= 10
    }

    if is_odd == false {
        result = 0
    }

    return result
}



