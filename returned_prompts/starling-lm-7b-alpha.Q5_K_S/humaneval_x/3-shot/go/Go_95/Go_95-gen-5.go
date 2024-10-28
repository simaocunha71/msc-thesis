    keys := make([]string, 0)

    for k := range dict {
        keys = append(keys, k.(string))
    }

    lower_case := strings.ToLower(keys[0])
    upper_case := strings.ToUpper(keys[0])

    for _, key := range keys {
        if key != lower_case && key != upper_case {
            return false
        }
    }
    return true
}



