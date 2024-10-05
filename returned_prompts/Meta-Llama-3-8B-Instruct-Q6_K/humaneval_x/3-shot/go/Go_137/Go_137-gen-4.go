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
                return a
            } else if a.(int) < b {
                return b
            } else {
                return nil
            }
        case string:
            s, _ := strconv.ParseFloat(b.(string), 64)
            if a.(int) > s {
                return a
            } else if a.(int) < s {
                return b
            } else {
                return nil
            }
        }
    case float64:
        switch b.(type) {
        case int:
            if a > b.(int) {
                return a
            } else if a < b.(int) {
                return b
            } else {
                return nil
            }
        case float64:
            if a > b {
                return a
            } else if a < b {
                return b
            } else {
                return nil
            }
        case string:
            s, _ := strconv.ParseFloat(b.(string), 64)
            if a > s {
                return a
            } else if a < s {
                return b
            } else {
                return nil
            }
        }
    case string:
        switch b.(type) {
        case int:
            s, _ := strconv.ParseFloat(a.(string), 64)
            if s > b.(int) {
                return a
            } else if s < b.(int) {
                return b
            } else {
                return nil
            }
        case float64:
            s, _ := strconv.ParseFloat(a.(string), 64)
            if s > b {
                return a
            } else if s < b {
                return b
            } else {
                return nil
            }
        case string:
            s1, _ := strconv.ParseFloat(a.(string), 64)
            s2, _ := strconv.ParseFloat(b.(string), 64)
            if s1 > s2 {
                return a
            } else if s1 < s2 {
                return b
            } else {
                return nil
            }
        }
    }
    return nil
