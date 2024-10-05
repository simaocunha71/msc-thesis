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
            num, err := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64)
            if err != nil {
                return nil
            }
            if a.(int) > num {
                return a
            } else if a.(int) < num {
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
            num, err := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64)
            if err != nil {
                return nil
            }
            if a > num {
                return a
            } else if a < num {
                return b
            } else {
                return nil
            }
        }
    case string:
        switch b.(type) {
        case int:
            num, err := strconv.ParseFloat(strings.Replace(a.(string), ",", ".", -1), 64)
            if err != nil {
                return nil
            }
            if num > float64(b.(int)) {
                return a
            } else if num < float64(b.(int)) {
                return b
            } else {
                return nil
            }
        case float64:
            num, err := strconv.ParseFloat(strings.Replace(a.(string), ",", ".", -1), 64)
            if err != nil {
                return nil
            }
            if num > b {
                return a
            } else if num < b {
                return b
            } else {
                return nil
            }
