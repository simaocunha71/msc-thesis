    if len(dict)==0 {
        return false
    }

    all_strings := true
    for k, _ := range dict {
        if _, ok := k.(string); !ok {
            all_strings = false
            break
        }
        if strings.ToLower(k.(string)) != k.(string) && strings.ToUpper(k.(string)) != k.(string) {
            all_strings = false
            break
        }
    }
    return all_strings
}



