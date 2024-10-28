    switch a := a.(type) {
    case int:
        if b, ok := b.(int); ok {
            if a > b {
                return a
            } else if a < b {
                return b
            }
        }
    case float64:
        if b, ok := b.(float64); ok {
            if a > b {
                return a
            } else if a < b {
                return b
            }
        }
    case string:
        if b, ok := b.(string); ok {
            aFloat, err1 := strconv.ParseFloat(strings.Replace(a, ",", ".", -1), 64)
            bFloat, err2 := strconv.ParseFloat(strings.Replace(b, ",", ".", -1), 64)
            if err1 != nil || err2 != nil {
                return nil
            }
            if aFloat > bFloat {
                return a
            } else if aFloat < bFloat {
                return b
            }
        }
    default:
        return nil
    }
    return nil
}



