    if len(dict) == 0 {
        return false
    }
    firstKey := ""
    for k := range dict {
        if firstKey == "" {
            firstKey = strings.ToLower(string(k.([]byte)))
        } else {
            if strings.ToLower(string(k.([]byte))) != firstKey {
                return false
            }
        }
    }
    return true
}