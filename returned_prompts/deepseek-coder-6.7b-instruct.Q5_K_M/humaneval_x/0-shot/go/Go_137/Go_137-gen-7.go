    switch a := a.(type) {
    case int:
        if b, ok := b.(int); ok {
            if a > b {
                return a
            } else if a == b {
                return nil
            } else {
                return b
            }
        }
    case float64:
        if b, ok := b.(float64); ok {
            if a > b {
                return a
            } else if a == b {
                return nil
            } else {
                return b
            }
        }
    case string:
        switch b := b.(type) {
        case string:
            aFloat, err := strconv.ParseFloat(strings.Replace(a, ",", ".", -1), 64)
            if err != nil