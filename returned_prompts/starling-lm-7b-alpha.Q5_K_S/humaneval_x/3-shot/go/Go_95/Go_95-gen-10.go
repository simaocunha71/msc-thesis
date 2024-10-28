    keys := make([]string, 0)
    for k := range dict {
        keys = append(keys, k.(string))
    }
    if len(keys) == 0 {
        return false
    }
    first_key := strings.ToLower(keys[0])
    for _, key := range keys {
        if key != first_key && key != strings.ToUpper(first_key) {
            return false
        }
    }
    return true
}



