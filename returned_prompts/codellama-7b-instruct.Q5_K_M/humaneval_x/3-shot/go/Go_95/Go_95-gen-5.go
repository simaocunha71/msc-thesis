    if len(dict) == 0 {
        return false
    }

    for key, _ := range dict {
        if str_key, ok := key.(string); ok {
            if strings.ToLower(str_key) != str_key {
                return false
            }
        } else {
            return false
        }
    }
    return true
}



