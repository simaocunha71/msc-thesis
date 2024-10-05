    min_val := math.Inf(1)
    max_val := math.Inf(-1)

    for _, v := range lst {
        if v < 0 && v < min_val {
            min_val = float64(v)
        }
        if v > 0 && v > max_val {
            max_val = float64(v)
        }
    }

    return [2]interface{}{min_val == math.Inf(1) ? nil : min_val, max_val == math.Inf(-1) ? nil : max_val}
}



