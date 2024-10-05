    var aFloat float64
    var bFloat float64
    var aStr string
    var bStr string

    switch v := a.(type) {
    case int:
        aFloat = float64(v)
    case string:
        aStr = v
    case float64:
        aFloat = v
    default:
        panic("unexpected type")
    }

    switch v := b.(type) {
    case int:
        bFloat = float64(v)
    case string:
        bStr = v
    case float64:
        bFloat = v
    default:
        panic("unexpected type")
    }

    if aStr != "" {
        aStr = strings.ReplaceAll(aStr, ",", ".")
        aFloat, _ = strconv.ParseFloat(aStr, 64)
    }

    if bStr != "" {
        bStr = strings.ReplaceAll(bStr, ",", ".")
        bFloat, _ = strconv.ParseFloat(bStr, 64)
    }

    if aFloat > bFloat {
        return a
    } else if aFloat < bFloat {
        return b
    } else {
        return nil
    }
}