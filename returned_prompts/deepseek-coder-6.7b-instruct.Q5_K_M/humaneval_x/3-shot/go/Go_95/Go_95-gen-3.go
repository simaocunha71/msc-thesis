    if len(dict) == 0 {
        return false
    }

    lower, upper := true, true

    for k := range dict {
        if s, ok := k.(string); ok {
            if !strings.EqualFold(s, s) {
                lower = false
            }
            if s != strings.ToLower(s) {
                upper = false
            }
            if !lower && !upper {
                break
            }
        } else {
            return false
        }
    }

    return lower || upper
}



