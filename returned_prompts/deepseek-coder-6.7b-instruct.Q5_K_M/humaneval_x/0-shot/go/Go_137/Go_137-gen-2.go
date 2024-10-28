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
        if b, ok := b.(string); ok {
            a, _ := strconv.ParseFloat(strings.Replace(a