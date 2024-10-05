    if a == b {
        return nil
    }

    var aStr, bStr string
    var aFloat, bFloat float64

    switch a.(type) {
    case string:
        aStr = a.(string)
        bStr = b.(string)

        var aInt, bInt int
        fmt.Sscanf(aStr, "%d", &aInt)
        fmt.Sscanf(bStr, "%d", &bInt)

        if aInt > bInt {
            return a
        } else {
            return b
        }
    case float64:
        aFloat = a.(float64)
        bFloat = b.(float64)

        if aFloat > bFloat {
            return a
        } else {
            return b
        }
    default:
        goto A
    }

    return nil
}

