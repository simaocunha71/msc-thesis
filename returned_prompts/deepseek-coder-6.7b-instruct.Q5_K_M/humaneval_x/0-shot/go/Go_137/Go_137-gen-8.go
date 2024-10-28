    switch a := a.(type) {
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
            if float64(a) > b {
                return float64(a)
            } else if float64(a) == b {
                return nil
            } else {
                return b
            }
        case string:
            aFloat, _ := strconv.ParseFloat(strings.Replace(a, ",", ".", -1), 64)
            bFloat, _ := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64)
            if aFloat > bFloat {
                return a
            } else if aFloat == bFloat {
                return nil
            } else {
                return b
            }
        }
    case float64:
        switch b := b.(type) {
        case int:
            if a > float64(b) {
                return a
            } else if a == float64(b) {
                return nil
            } else {
                return float64(b)
            }
        case float64:
            if a > b {
                return a
            } else if a == b {
                return nil
            } else {
                return b
            }
        case string:
            aFloat, _ := strconv.ParseFloat(strings.Replace(a, ",", ".", -1), 64)
            bFloat, _ := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64)
            if aFloat > bFloat {
                return a
            } else if aFloat == bFloat {
                return nil
            } else {
                return b
            }
        }
    case string:
        switch b := b.(type) {
        case int:
            aFloat, _ := strconv.ParseFloat(strings.Replace(a, ",", ".", -