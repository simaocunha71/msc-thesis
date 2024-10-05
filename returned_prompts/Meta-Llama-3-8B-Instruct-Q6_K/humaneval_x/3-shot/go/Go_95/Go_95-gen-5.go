    for key, _ := range dict {
        key_str := fmt.Sprintf("%v", key)
        if !strings.EqualFold(key_str, strings.ToLower(key_str)) && !strings.EqualFold(key_str, strings.ToUpper(key_str)) {
            return false
        }
    }
    return true
}