    for key := range dict {
        str_key := fmt.Sprintf("%v", key)
        if !strings.EqualFold(str_key, strings.ToUpper(str_key)) && !strings.EqualFold(str_key, strings.ToLower(str_key)) {
            return false
        }
    }
    return true
}