    allLower := true
    allUpper := true
    for key, _ := range dict {
        if _, ok := key.(string); ok {
            if strings.ToLower(string(key.(string))) != string(key.(string)) {
                allLower = false
            }
            if strings.ToUpper(string(key.(string))) != string(key.(string)) {
                allUpper = false
            }
        } else {
            return false
        }
    }
    return allLower || allUpper
}  // CheckDictCase
} // package main


