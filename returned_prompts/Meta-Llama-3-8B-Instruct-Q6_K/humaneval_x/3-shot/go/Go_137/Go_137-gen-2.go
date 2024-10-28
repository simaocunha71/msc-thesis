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
            str_b, _ := strconv.ParseFloat(b.(string), 64)
            if a.(int) > str_b {
                return a
            } else if a.(int) < str_b {
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
            str_b, _ := strconv.ParseFloat(b.(string), 64)
            if a > str_b {
                return a
            } else if a < str_b {
                return b
            } else {
                return nil
            }
        }
    case string:
        switch b.(type) {
        case int:
            str_a, _ := strconv.ParseFloat(a.(string), 64)
            if str_a > b.(int) {
                return a
            } else if str_a < b.(int) {
                return b
            } else {
                return nil
            }
        case float64:
            str_a, _ := strconv.ParseFloat(a.(string), 64)
            if str_a > b {
                return a
            } else if str_a < b {
                return b
            } else {
                return nil
            }
        case string:
            str_a, _ := strconv.ParseFloat(a.(string), 64)
            str_b, _ := strconv.ParseFloat(b.(string), 64)
            if str_a > str_b {
                return a
            } else if str_a < str_b {
                return b
            } else {
                return