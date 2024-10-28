    result := 1
    for n > 0 {
        last_digit := n % 10
        if last_digit % 2 == 1 {
            result *= last_digit
        }
        n /= 10
    }
    return result
}



