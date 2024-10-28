    result := make([]float64, 0)
    for _, v := range lst {
        if v > 0 && math.Floor(v) == v {
            result = append(result, v*v)
        }
    }
    return int(sum(result))
}



