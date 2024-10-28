    switch a := a.(type) {
    case int:
        switch b := b.(type) {
        case float64:
            if float64(a) > b {
                return float64(a)
            } else if float64(a) == b {
                return nil
            } else {
                return b
            }
        case string:
            if strings.Contains(b, ".") {
                b = strings.Replace(b, ",", ".", -1)
            }
            b, _ := strconv.ParseFloat(b, 64)
            if float64(a) > b {
                return float64(a)
            } else if float64(a) == b {
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
        case string:
            if strings.Contains(b, ".") {
                b = strings.Replace(b, ",", ".", -1)
            }
            b, _ := strconv.ParseFloat(b, 64)
            if a > b {
                return a
            } else if a == b {
                return nil
            } else {
                return b
            }
        }
    case string:
        if strings.Contains(a, ".") {
            a = strings.Replace(a, ",", ".", -1)
        }
        a, _ := strconv.ParseFloat(a, 64)
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
            } else if a == b