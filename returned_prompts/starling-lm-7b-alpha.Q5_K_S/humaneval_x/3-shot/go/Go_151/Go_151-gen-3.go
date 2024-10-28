    result := 0
    for _, v := range lst {
        if v != 0 && v == math.Floor(v) && v % 2 == 1 {
            result += v * v
        }
    }
    return result
}



