    var result int = 0

    for _, v := range arr[:k] {
        if v < 10 {
            result += v
        } else if v < 100 {
            result += v % 10
        }
    }

    return result
}

