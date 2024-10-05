    if a == nil && b == nil {
        return nil
    }

    if a == nil {
        return b
    }

    if b == nil {
        return a
    }

    switch a.(type) {
    case int:
        switch b.(type) {
        case int:
            if a.(int) > b.(int) {
                return a
            }
            if a.(int) < b.(int) {
                return b
            }
            return nil
        case float64:
            if float64(a.(int)) > b.(float64) {
                return a
            }
            if float64(a.(int)) < b.(float64) {
                return b
            }
            return nil
        case string:
            if a.(int) > parse_float(b.(string)) {
                return a
            }
            if a.(int) < parse_float(b.(string)) {
                return b
            }
            return nil
        }
    case float64:
        switch b.(type) {
        case int:
            if a.(float64) > float64(b.(int)) {
                return a
            }
            if a.(float64) < float64(b.(int)) {
                return b
            }
            return nil
        case float64:
            if a.(float64) > b.(float64) {
                return a
            }
            if a.(float64) < b.(float64) {
                return b
            }
            return nil
        case string:
            if a.(float64) > parse_float(b.(string)) {
                return a
            }
            if a.(float64) < parse_float(b.(string)) {
                return b
            }
            return nil
        }
    case string:
        switch b.(type) {
        case int:
            if parse_float(a.(string)) > float64(b.(int)) {
                return a
            }
            if parse_float(a.(string)) < float64(b.(int)) {
                return b
