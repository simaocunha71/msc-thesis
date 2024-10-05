    for k, _ := range dict {
        if k.(string) == strings.ToLower(k.(string)) {
            continue
        } else if k.(string) == strings.ToUpper(k.(string)) {
            continue
        } else {
            return false
        }
    }
    return true
}

