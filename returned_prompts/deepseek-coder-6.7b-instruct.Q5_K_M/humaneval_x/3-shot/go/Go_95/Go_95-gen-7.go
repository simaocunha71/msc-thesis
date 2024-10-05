    if len(dict) == 0 {
        return false
    }

    keys := make([]string, 0, len(dict))
    for key := range dict {
        keys = append(keys, key.(string))
    }

    if len(keys) == 0 {
        return false
    }

    firstKey := keys[0]

    return strings.ToLower(firstKey) == firstKey || strings.ToUpper(firstKey) == firstKey
}



