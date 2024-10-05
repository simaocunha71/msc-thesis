    for k, _ := range dict {
        switch k.(type) {
        case string:
            if !strings.EqualFold(k.(string), k.(string)) {
                continue A
            }
        default:
            return false
        }
    }
    return true
}
