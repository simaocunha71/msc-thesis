    if len(dict) == 0 {
        return false
    }

    all_lowercase := true
    all_uppercase := true

    for k, v := range dict {
        if kstr, ok := k.(string); ok {
            if kstr != strings.ToLower(kstr) && kstr != strings.ToUpper(kstr) {
                return false
            }
            if kstr != strings.ToLower(kstr) {
                all_lowercase = false
            }
            if kstr != strings.ToUpper(kstr) {
                all_uppercase = false
            }
        } else {
            return false
        }
    }
    return all_lowercase || all_uppercase
}



