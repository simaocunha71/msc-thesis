    for k, _ := range dict {
        k_str := k.(string)
        if strings.ToLower(k_str) != k_str && strings.ToUpper(k_str) != k_str {
            return false
        }
    }
    return true
}



