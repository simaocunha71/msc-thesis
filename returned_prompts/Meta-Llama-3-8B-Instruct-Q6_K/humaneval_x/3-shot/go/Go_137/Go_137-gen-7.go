    switch a.(type) {
    case int:
        switch b.(type) {
        case int:
            if a.(int) > b.(int) {
                return a
            } else if a.(int) < b.(int) {
                return b
            } else {
                return nil
            }
        case float64:
            if a.(int) > b {
                return b
            } else {
                return a
            }
        case string:
            if strings.Contains(b.(string), ",") {
                bFloat, _ := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64)
                if a.(int) > bFloat {
                    return b
                } else {
                    return a
                }
            } else {
                bInt, _ := strconv.Atoi(b.(string))
                if a.(int) > bInt {
                    return b
                } else {
                    return a
                }
            }
        }
    case float64:
        switch b.(type) {
        case int:
            if a > b.(int) {
                return a
            } else {
                return b
            }
        case float64:
            if a > b {
                return a
            } else {
                return b
            }
        case string:
            if strings.Contains(b.(string), ",") {
                bFloat, _ := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64)
                if a > bFloat {
                    return a
                } else {
                    return b
                }
            } else {
                bInt, _ := strconv.Atoi(b.(string))
                if a > bInt {
                    return a
                } else {
                    return b
                }
            }
        }
    case string:
        switch b.(type) {
        case int:
            if strings.Contains(a.(string), ",") {
                aFloat, _ := strconv.ParseFloat(strings.Replace(a.(string), ",", ".", -1), 64)
                if aFloat > float64(b) {
                    return a
                } else {
                    return b
                }
            } else {
                aInt, _ := strconv.Atoi(a.(string))
                if aInt > b {
                    return a
                } else {
                    return b
                }
            }
        case float64:
            if strings.Contains(a.(string), ",") {
                aFloat, _ := strconv.ParseFloat(strings.Replace(a.(string), ",", ".", -1),