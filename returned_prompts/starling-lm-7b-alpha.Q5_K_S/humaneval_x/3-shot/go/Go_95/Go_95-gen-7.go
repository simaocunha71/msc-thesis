    keys := make([]string, 0)
    for k := range dict {
        keys = append(keys, k.(string))
    }

    if len(keys) == 0 {
        return false
    }

    if len(keys) == 1 {
        return true
    }

    lower := keys[0]
    upper := strings.ToUpper(lower)
    for _, k := range keys {
        if k != lower && k != upper {
            return false
        }
    }

    return true
}



