    if a == b {
        return nil
    }

    switch aType := a.(type) {
    case int:
        if float64(aType) > b.(float64) {
            return a
        } else {
            return b
        }
    case float64:
        if aType > b.(float64) {
            return a
        } else {
            return b
        }
    case string:
        if strings.HasPrefix(aType, "0.") || strings.HasPrefix(aType, "-0.") {
            aType = strings.Replace(aType, ".", "", -1)
            aType = strings.Replace(aType, ",", ".", -1)
        }
        if strings.HasPrefix(aType, "0") {
            aType = aType[1:]
        }

        if strings.HasPrefix(b.(string), "0.") || strings.HasPrefix(b.(string), "-0.") {
            b = strings.Replace(b.(string), ".", "", -1)
            b = strings.Replace(b.(string), ",", ".", -1)
        }
        if strings.HasPrefix(b.(string), "0") {
            b = b.(string)[1:]
        }

        if aType > b.(string) {
            return a
        } else {
            return b
        }
    }

    return nil
}



