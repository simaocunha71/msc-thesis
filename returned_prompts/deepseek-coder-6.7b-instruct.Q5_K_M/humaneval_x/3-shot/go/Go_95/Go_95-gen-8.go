    if len(dict) == 0 {
        return false
    }
    lower, upper := 0, 0
    for k := range dict {
        if key, ok := k.(string); ok {
            if strings.ToLower(key) == key {
                lower++
            } else if strings.ToUpper(key) == key {
                upper++
            }
        } else {
            return false
        }
    }
    return lower == 0 || upper == 0
}

