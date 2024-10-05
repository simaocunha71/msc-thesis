    for key := range dict {
        if _, ok := key.(string); ok {
            if strings.ToLower(key.(string)) != key.(string) && strings.ToUpper(key.(string)) != key.(string) {
                return false
            }
        } else {
            return false
        }
    }
    return true
}


