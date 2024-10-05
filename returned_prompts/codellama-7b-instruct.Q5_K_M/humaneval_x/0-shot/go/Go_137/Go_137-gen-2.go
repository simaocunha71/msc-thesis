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
        default:
            return nil
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
        default:
            return nil
        }
    case string:
        switch b.(type) {
        case int:
            return a
        case float64:
            return a
        case string:
            //if a.(string) > b.(string) {
            //    return a
            //}
            //if a.(string) < b.(string) {
            //    return b
            //}
            return nil
        default:
            return nil
        }
    default:
        return nil
    }

    return nil
}
