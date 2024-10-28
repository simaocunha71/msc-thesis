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
            }
            if a.(float64) < b.(float64) {
                return b
            }
            return nil
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
            a_float, _ := strconv.ParseFloat(strings.Replace(a.(string), ",", ".", 1), 64)
            b_float, _ := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", 1), 64)
            if a_float > b_float {
                return a
            }
            if a_float < b_float {
                return b
            }
            return nil
        }
    }
    return nil
}



