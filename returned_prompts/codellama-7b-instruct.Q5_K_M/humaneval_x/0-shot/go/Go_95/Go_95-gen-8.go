    for k, v := range dict {
        if _, ok := k.(string); !ok {
            continue A
        }
        if strings.ToLower(k.(string)) != k.(string) &&
            strings.ToUpper(k.(string)) != k.(string) {
            return false
        }
        if _, ok := v.(string); !ok {
            continue A
        }
        if strings.ToLower(v.(string)) != v.(string) &&
            strings.ToUpper(v.(string)) != v.(string) {
            return false
        }
    }
    return true
}
