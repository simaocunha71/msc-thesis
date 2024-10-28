    if len(dict)==0 {
        return false
    }
    keysUpper := true
    keysLower := true
    for k := range dict {
        if ks, ok := k.(string); ok {
            if !strings.EqualFold(ks, strings.ToUpper(ks)) {
                keysUpper = false
            }
            if !strings.EqualFold(ks, strings.ToLower(ks)) {
                keysLower = false
            }
        } else {
            return false
        }
    }
    return keysUpper || keysLower
}



