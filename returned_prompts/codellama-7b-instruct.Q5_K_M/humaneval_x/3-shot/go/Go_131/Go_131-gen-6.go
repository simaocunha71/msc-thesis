    var result int = 1

    for n > 0 {
        digit := n % 10
        if digit % 2 != 0 {
            result *= digit
        }
        n /= 10
    }

    return result
}



