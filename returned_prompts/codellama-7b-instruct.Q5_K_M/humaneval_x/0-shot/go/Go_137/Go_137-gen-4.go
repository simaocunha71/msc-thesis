    switch a := a.(type) {
    case int:
        switch b := b.(type) {
        case int:
            if a > b {
                return a
            } else if a < b {
                return b
            }
        case float64:
            return b
        case string:
            return b
        }
    case float64:
        switch b := b.(type) {
        case int:
            return a
        case float64:
            if a > b {
                return a
            } else if a < b {
                return b
            }
        case string:
            return b
        }
    case string:
        switch b := b.(type) {
        case int:
            return a
        case float64:
            return a
        case string:
            a = strings.ReplaceAll(a, ",", ".")
            b = strings.ReplaceAll(b, ",", ".")
            a_float, _ := strconv.ParseFloat(a, 64)
            b_float, _ := strconv.ParseFloat(b, 64)
            if a_float > b_float {
                return a
            } else if a_float < b_float {
                return b
            }
        }
    }
    return nil
}
