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
            b, _ := strconv.ParseFloat(strings.Replace(b, ",", ".", -1), 64)
            return compareFloats(a, b)
        }
    case string:
        switch b := b.(type) {
        case float64:
            a, _ := strconv.ParseFloat(strings.Replace(a, ",", ".", -1), 64)
            return compareFloats(a, b)
        case string:
            a = strings.Replace(a, ",", ".", -1)
            b = strings.Replace(b, ",", ".", -1)
            a_float, _ := strconv.ParseFloat(a, 64)
            b_float, _ := strconv.ParseFloat(b, 64)
            return compareFloats(a_float, b_float)
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
            return compareFloats(float64(a), b)
        case string:
            b, _ := strconv.ParseFloat(strings.Replace(b, ",", ".", -1), 64)
            return compareFloats(float64(a), b)
        }
    case int64:
        switch b := b.(type) {
        case int64:
            if a > b {
                return a
            } else if a == b {
                return nil
            } else {
                return b
            }
        case float64:
            return compareFloats(float64(a), b)
        case string:
            b, _ := strconv