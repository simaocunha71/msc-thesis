    var result int = 1
    for n > 0 {
        d := n % 10
        if d % 2 == 1 {
            result *= d
        }
        n = n / 10
    }
    return result
}



