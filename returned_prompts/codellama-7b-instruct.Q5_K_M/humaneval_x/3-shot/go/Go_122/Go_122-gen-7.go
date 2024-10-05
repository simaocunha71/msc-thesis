    result := 0
    for _, v := range arr[:k] {
        if v <= 100 {
            result += v
        }
    }
    return result
}



