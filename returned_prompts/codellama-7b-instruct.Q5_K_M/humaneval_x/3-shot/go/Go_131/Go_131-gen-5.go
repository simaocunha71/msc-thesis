    result := 0
    for ; n > 0; n /= 10 {
        digit := n % 10
        if digit % 2 != 0 {
            result *= digit
        }
    }
    return result
}



