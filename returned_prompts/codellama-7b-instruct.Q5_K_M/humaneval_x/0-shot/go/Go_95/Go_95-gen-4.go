    for k := range dict {
        v := k.(string)
        if strings.ToLower(v) == v {
            continue A
        }
        if strings.ToUpper(v) == v {
            continue A
        }
        return false
    }
    return true
}
