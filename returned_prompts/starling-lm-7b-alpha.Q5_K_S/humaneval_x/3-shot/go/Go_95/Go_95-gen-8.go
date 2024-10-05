    for key, value := range dict {
        if _, ok := key.(string); !ok {
            return false
        }
        if _, ok := value.(string); !ok {
            return false
        }
        if strings.ToLower(key.(string)) != key.(string) {
            return false
        }
    }
    return true
}



