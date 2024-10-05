    result := 0
    for i, v := range lst {
        if i % 2 == 1 && v % 2 == 0 {
            result += v
        }
    }
    return result
}



