    for key := range dict {

        switch key := key.(type) {
        case string:
            if !(strings.ToLower(key) == key || strings.ToUpper(key) == key) {
                return false
            }
        default:
            return false
        }
    }
    return true