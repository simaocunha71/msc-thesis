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
            return b
        case string:
            return b
        }
    case float64:
        switch b.(type) {
        case int:
            return a
        case float64:
            if a.(float64) > b.(float64) {
                return a
            } else if a.(float64) < b.(float64) {
                return b
            } else {
                return nil
            }
        case string:
            return b
        }
    case string:
        switch b.(type) {
        case int:
            return a
        case float64:
            return a
        case string:
            if strings.Compare(a.(string), b.(string)) > 0 {
                return a
            } else if strings.Compare(a.(string), b.(string)) < 0 {
                return b
            } else {
                return nil
            }
        }
    }

    return nil
}



