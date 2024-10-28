    if len(dict) == 0 {
        return false
    }
    lower := 0
    upper := 0
    for k, _ := range dict {
        if k == strings.ToLower(k.(string)) {
            lower += 1
        }else if k == strings.ToUpper(k.(string)) {
            upper += 1
        }else {
            return false
        }
    }
    if lower != 0 && upper != 0 {
        return true
    }
    return false
}



