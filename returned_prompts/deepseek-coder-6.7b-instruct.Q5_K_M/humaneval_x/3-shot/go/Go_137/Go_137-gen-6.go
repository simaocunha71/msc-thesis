    switch a := a.(type) {
    case float64:
        switch b := b.(type) {
        case float64:
            if a > b {
                return a
            } else if a == b {
                return nil
            } else {
                return b
            }
        case string:
            b, _ := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64)
            return math.Max(a, b)
        }
    case string:
        a, _ := strconv.ParseFloat(strings.Replace(a.(string), ",", ".", -1), 64)
        switch b := b.(type) {
        case float64:
            return math.Max(a, b)
        case string:
            b, _ := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64)
            return math.Max(a, b)
        }
    case int:
        switch b := b.(type) {
        case int:
            if a > b {
                return a
            } else if a == b {
                return nil
            } else {
                return b
            }
        case float64:
            return math.Max(float64(a), b)
        case string:
            b, _ := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64)
            return math.Max(float64(a), b)
        }
    }
    return nil
}



