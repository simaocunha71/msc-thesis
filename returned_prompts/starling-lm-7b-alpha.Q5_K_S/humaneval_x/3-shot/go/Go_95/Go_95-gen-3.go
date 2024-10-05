    keys := make([]string, 0)
    for k := range dict {
        keys = append(keys, k.(string))
    }
    if len(keys) == 0 {
        return false
    }
    is_lower := true
    is_upper := true
    for _, key := range keys {
        if !strings.EqualFold(key, strings.ToLower(key)) {
            is_lower = false
        }
        if !strings.EqualFold(key, strings.ToUpper(key)) {
            is_upper = false
        }
    }
    return is_lower || is_upper
}




