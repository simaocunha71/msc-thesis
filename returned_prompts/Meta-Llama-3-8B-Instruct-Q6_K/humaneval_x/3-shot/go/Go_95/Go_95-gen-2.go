    if len(dict) == 0 {
        return false
    }
    keys := make([]string, 0)
    for k := range dict {
        keys = append(keys, k.(string))
    }
    allLower := true
    allUpper := true
    for _, key := range keys {
        if !strings.HasSuffix(key, "upper") && !strings.HasSuffix(key, "lower") {
            if strings.ToLower(key) != key {
                allLower = false
            }
            if strings.ToUpper(key) != key {
                allUpper = false
            }
        }
    }
    return allLower || allUpper
}