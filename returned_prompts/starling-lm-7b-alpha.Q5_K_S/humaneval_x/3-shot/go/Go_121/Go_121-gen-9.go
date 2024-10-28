    result := 0
    for i, v := range lst {
        if v % 2 == 0 && i % 2 == 0 {
            result += v
        }
    }
    return result
}



