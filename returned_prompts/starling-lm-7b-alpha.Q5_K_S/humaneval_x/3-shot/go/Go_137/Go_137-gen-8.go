    if a == b {
        return nil
    }
    if _, ok := a.(string); ok {
        a, _ = strconv.ParseFloat(a.(string), 64)
    }
    if _, ok := b.(string); ok {
        b, _ = strconv.ParseFloat(b.(string), 64)
    }
    if a.(float64) > b.(float64) {
        return a
    } else {
        return b
    }
}



