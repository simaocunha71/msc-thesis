    result := 0
    for _, v := range lst {
        if v > 0 && math.Trunc(v) == v {
            result += v*v
        }
    }
    return result
}



