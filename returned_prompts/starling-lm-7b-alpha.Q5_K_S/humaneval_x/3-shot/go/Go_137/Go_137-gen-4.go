    if a == nil {
        return b
    }
    if b == nil {
        return a
    }
    a_str, _ := strconv.ParseFloat(fmt.Sprintf("%v", a), 64)
    b_str, _ := strconv.ParseFloat(fmt.Sprintf("%v", b), 64)
    if math.Abs(a_str-b_str) < 0.0000000001 {
        return nil
    }
    if a_str > b_str {
        return a
    }
    return b
}



