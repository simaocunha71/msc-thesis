    if len(dict) == 0 {
        return false
    }

    lower, upper := true, true

    for key := range dict {
        if keyStr, ok := key.(string); ok {
            if keyStr != strings.ToLower(keyStr) {
                lower = false
            }
            if keyStr != strings.ToUpper(keyStr) {
                upper = false
            }

            if !lower && !upper {
                return false
            }
        } else {
            return false
        }
    }

    return true
}



