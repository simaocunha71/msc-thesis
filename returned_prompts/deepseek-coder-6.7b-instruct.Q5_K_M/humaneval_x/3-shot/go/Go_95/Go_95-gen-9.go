    if len(dict) == 0 {
        return false
    }

    lower_case := true
    upper_case := true

    for key := range dict {
        switch key := key.(type) {
        case string:
            if !strings.IsLower(key) {
                lower_case = false
            }
            if !strings.IsUpper(key) {
                upper_case = false
            }
        default:
            return false
        }
    }

    return lower_case || upper_case
}



