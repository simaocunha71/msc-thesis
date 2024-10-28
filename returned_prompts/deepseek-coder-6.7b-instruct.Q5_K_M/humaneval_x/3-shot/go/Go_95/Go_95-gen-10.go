    if len(dict) == 0{
        return false
    }

    keysAreLower := true
    keysAreUpper := true

    for key := range dict {
        if !strings.EqualFold(key.(string), strings.ToLower(key.(string))){
            keysAreLower = false
        }
        if !strings.EqualFold(key.(string), strings.ToUpper(key.(string))){
            keysAreUpper = false
        }
    }

    return keysAreLower || keysAreUpper
}



