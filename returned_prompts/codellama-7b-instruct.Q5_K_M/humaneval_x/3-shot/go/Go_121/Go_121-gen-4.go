    result := 0
    for i, e := range lst {
        if i%2 == 0 && e%2 != 0 {
            result += e
        }
    }
    return result
}



