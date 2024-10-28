    if len(dict) == 0 {
        return false
    }

    keys := make([]string, 0, len(dict))
    for k := range dict {
        keys = append(keys, k.(string))
    }

    all_lowercase := true
    all_uppercase := true
    for _, k := range keys {
        if strings.ToLower(k) != k {
            all_lowercase = false
        }
        if strings.ToUpper(k) != k {
            all_uppercase = false
        }
    }
    if all_lowercase || all_uppercase {
        return true
    }
    return false
}



