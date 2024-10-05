    var maxVal interface{}
    switch a := a.(type) {
    case int:
        if b, ok := b.(int); ok {
            if a > b {
                maxVal = a
            } else if a == b {
                maxVal = nil
            } else {
                maxVal = b
            }
        }
    case float64:
        if b, ok := b.(float64); ok {
            if a > b {
                maxVal = a
            } else if a == b {
                maxVal = nil
            } else {
                maxVal = b
            }
        }
    case string:
        if b, ok := b.(string); ok {
            aFloat, err1 := strconv.ParseFloat(strings.Replace(a, ",", ".", -1), 64)
            bFloat, err2 := strconv.ParseFloat(strings.Replace(b, ",", ".", -1), 64)
            if err1 != nil || err2 != nil {
                fmt.Println("Error: Not a valid number string")
                return nil
            }

            if aFloat > bFloat {
                maxVal = a
            } else if aFloat == bFloat {
                maxVal = nil
            } else {
                maxVal = b
            }
        }
    default:
        fmt.Println("Error: Type not supported")
        return nil
    }
    return maxVal
}



