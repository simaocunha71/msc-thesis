```go
func CompareOne(a, b interface{}) interface{} {
    switch a.(type) {
    case int:
        aFloat := float64(a.(int))
        switch b.(type) {
        case int:
            bFloat := float64(b.(int))
            if aFloat > bFloat {
                return a
            } else if aFloat < bFloat {
                return b
            }
        case float64:
            if aFloat > b {
                return a
            } else if aFloat < b {
                return b
            }
        case string:
            bFloat, err := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", 1), 64)
            if err != nil {
                return nil
            }
            if aFloat > bFloat {
                return a
            } else if aFloat < bFloat {
                return b
            }
        default:
            return nil
        }
    case float64:
        aFloat := a.(float64)
        switch b.(type) {
        case int:
            bFloat := float64(b.(int))
            if aFloat > bFloat {
                return a
            } else if aFloat < bFloat {
                return b
            }
        case float64:
            if aFloat > b {
                return a
            } else if aFloat < b {
                return b
            }
        case string:
            bFloat, err := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", 1), 64)
            if err != nil {
                return nil
            }
            if aFloat > bFloat {
                return a
            } else if aFloat < bFloat {
                return b
            }
        default:
            return nil
        }
    case string:
        aFloat, err := strconv.ParseFloat(strings.Replace(a.(string), ",", ".", 1), 64)
        if err != nil {
            return nil
        }
        switch b.(type) {
        case int:
            bFloat := float64(b.(int))
            if aFloat > bFloat {
                return a
            } else if aFloat < bFloat {
                return b
            }
        case float64:
            if aFloat > b {
                return a
            } else if aFloat < b {
                return b
            }
        case string:
            bFloat, err := strconv.ParseFloat(strings.Replace(b.(string), ",", ".", 1), 64)
            if err != nil