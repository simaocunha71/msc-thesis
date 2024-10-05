    if len(dict) == 0 {
        return false
    }
    var isLower bool = true
    for key := range dict {
        if _, ok := key.(string); !ok {
            return false
        }
        if strings.ToUpper(key.(string)) != key.(string) {
            isLower = false
        }
        if strings.ToLower(key.(string)) != key.(string) {
            isLower = false
        }
    }
    return isLower
}