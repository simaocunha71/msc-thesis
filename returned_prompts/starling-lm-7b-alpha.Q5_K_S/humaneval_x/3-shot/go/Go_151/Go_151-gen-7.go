    result := 0
    for _, v := range lst {
        if v > 0 && v - int(v) == 0 {
            result += v * v
        }
    }
    return result
}



