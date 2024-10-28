    result := 1
    is_odd := true

    for n > 0 {
        digit := n % 10

        if digit % 2 == 0 {
            is_odd = false
        }

        if is_odd {
            result *= digit
        }

        n /= 10
    }

    return result
}



