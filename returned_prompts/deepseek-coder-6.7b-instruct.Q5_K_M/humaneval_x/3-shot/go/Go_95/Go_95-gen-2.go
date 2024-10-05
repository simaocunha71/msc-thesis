    if len(dict) == 0 {
        return false
    }

    var allLowerCase bool = true
    var allUpperCase bool = true

    for key := range dict {
        switch key.(type) {
        case string:
            if !strings.EqualFold(key.(string), strings.ToLower(key.(string))) {
                allLowerCase = false
            }
            if !strings.EqualFold(key.(string), strings.ToUpper(key.(string))) {
                allUpperCase = false
            }
        default:
            return false
        }
    }

    return allLowerCase || allUpperCase
}



