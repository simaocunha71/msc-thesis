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
            if a.(int) > strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64) {
                return a
            } else if a.(int) < strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64) {
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
            if a > strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64) {
                return a
            } else if a < strconv.ParseFloat(strings.Replace(b.(string), ",", ".", -1), 64) {
                return b
            } else {
                return nil
            }
        }
    case string:
        switch b.(type) {
        case int:
            if strconv.ParseFloat(strings.Replace(a.(string), ",", ".", -1), 64) > b.(int) {
                return a
            } else if strconv.ParseFloat(strings.Replace(a.(string), ",", ".", -1), 64) < b.(int) {
                return b
            } else {
                return nil
            }
        case float64:
            if strconv.ParseFloat(strings.Replace(a.(string), ",", ".", -1), 64) > b {
                return a
            } else if strconv.ParseFloat(strings.Replace(a.(string), ",", ".", -1), 64) < b {
                return b
            } else {
                return nil
            }
        case string:
            if a.(string) > b