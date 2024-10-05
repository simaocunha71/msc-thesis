    result := 1
    for n > 0 {
        if n % 2 != 0 {
            result *= n % 10
        }
        n /= 10
    }
    return result
}



