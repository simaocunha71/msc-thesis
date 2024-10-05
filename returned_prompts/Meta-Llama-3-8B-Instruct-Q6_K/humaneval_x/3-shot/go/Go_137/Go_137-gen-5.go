    switch aType := a.(type); aType {
    case int:
        switch bType := b.(type) {
        case int:
            if a.(int) > b.(int) {
                return b
            } else if a.(int) < b.(int) {
                return a
            } else {
                return nil
            }
        case float64:
            if a.(int) > b {
                return b
            } else if a.(int) < b {
                return a
            } else {
                return nil
            }
        case string:
            // Handle string conversion
            aFloat, err := strconv.ParseFloat(a.(string), 64)
            bFloat, err := strconv.ParseFloat(b.(string), 64)
            if aFloat > bFloat {
                return b
            } else if aFloat < bFloat {
                return a
            } else {
                return nil
            }
        default:
            return nil
    }
    case float64:
        switch bType := b.(type) {
        case int:
            if a > b.(int) {
                return b
            } else if a < b.(int) {
                return a
            } else {
                return nil
            }
        case float64:
            if a > b {
                return b
            } else if a < b {
                return a
            } else {
                return nil
            }
        case string:
            // Handle string conversion
            aFloat, err := strconv.ParseFloat(a.(float64).String(), 64)
            bFloat, err := strconv.ParseFloat(b.(string), 64)
            if aFloat > bFloat {
                return b
            } else if aFloat < bFloat {
                return a
            } else {
                return nil
            }
        default:
            return nil
    }
    case string:
        // Handle string conversion
        aFloat, err := strconv.ParseFloat(a.(string), 64)
        bFloat, err := strconv.ParseFloat(b.(string), 64)
        if aFloat > bFloat {
            return b
        } else if aFloat < bFloat {
            return a
        } else {
            return nil
        }
    default:
        return nil
    }
}

func main() {
    fmt.Println(CompareOne(1, 2.5)) // 2.5
    fmt.Println(CompareOne(1, "2,