	// Write your code here.
    if len(dict) == 0 {
        return false
    }
    lower := false
    for k, v := range dict {
        switch v.(type) {
        case string:
            if strings.ToLower(v.(string)) != v.(string) {
                if lower {
                    return false
                } else {
                    lower = true
                }
            }
        default:
            return false
        }
        switch k.(type) {
        case string:
            if strings.ToLower(k.(string)) != k.(string) {
                if lower {
                    return false
                } else {
                    lower = true
                }
            }
        default:
            return false
        }
    }
    return true
}
