    result := 1
    for n > 0 {
        if n%2 == 1 {
            result = (result * p) % n
        }
        p = (p * p) % n
        n /= 2
    }
    return result
}



