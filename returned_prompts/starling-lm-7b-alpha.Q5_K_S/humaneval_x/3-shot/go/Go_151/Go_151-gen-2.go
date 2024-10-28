    result := 0
    for _, v := range lst {
        if v >= 0 && math.Ceil(v) == v && math.Floor(v) == v {
            if v % 2 == 1 {
                result += v*v
            }
        }
    }
    return result
}



