    for k, _ := range dict {
        switch k.(type) {
        case string:
            if strings.ToUpper(k.(string)) != k.(string) {
                continue A
            }
        default:
            return false
        }
    }
    return true
}

