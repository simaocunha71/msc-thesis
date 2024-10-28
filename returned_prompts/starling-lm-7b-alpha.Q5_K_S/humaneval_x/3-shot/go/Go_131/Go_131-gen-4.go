    result := 1
    for ; n > 0; n /= 10 {
        d := n % 10
        if d % 2 == 1 {
            result *= d
        }
    }
    return result
}



