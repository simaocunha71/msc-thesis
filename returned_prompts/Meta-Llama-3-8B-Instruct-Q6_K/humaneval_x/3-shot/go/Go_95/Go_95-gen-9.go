    for _, key := range dict {
        if _, ok := key.(string); !ok {
            return false
        }
        if strings.ToLower(string(key.(string))) != string(key.(string)) &&
            strings.ToUpper(string(key.(string))) != string(key.(string)) {
            return false
        }
    }
    return true
}