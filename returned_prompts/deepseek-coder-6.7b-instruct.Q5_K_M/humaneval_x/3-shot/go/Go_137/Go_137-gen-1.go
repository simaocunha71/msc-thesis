    var aFloat, bFloat float64
    var aString, bString string
    var aOk, bOk bool

    switch a := a.(type)  {
    case float64:
        aFloat = a
    case string:
        aString = a
        aFloat, aOk = strconv.ParseFloat(strings.Replace(aString, ",", ".", -1), 64)
    case int:
        aFloat = float64(a)
    }

    switch b := b.(type)  {
    case float64:
        bFloat = b
    case string:
        bString = b
        bFloat, bOk = strconv.ParseFloat(strings.Replace(bString, ",", ".", -1), 64)
    case int:
        bFloat = float64(b)
    }

    if !aOk || !bOk {
        return nil
    }

    switch {
    case aFloat > bFloat:
        return a
    case aFloat < bFloat:
        return b
    default:
        return nil
    }
}



