    keys := make([]string, 0)
    for key := range dict {
        keys = append(keys, key.(string))
    }
    lowerKeys := make([]string, 0)
    upperKeys := make([]string, 0)
    for _, key := range keys {
        if strings.ToLower(key) == key {
            lowerKeys = append(lowerKeys, key)
        }else if strings.ToUpper(key) == key {
            upperKeys = append(upperKeys, key)
        }else {
            return false
        }
    }
    return len(lowerKeys) == len(keys) || len(upperKeys) == len(keys)
}



