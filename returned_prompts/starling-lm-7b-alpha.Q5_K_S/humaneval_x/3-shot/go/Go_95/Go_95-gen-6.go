    if len(dict) == 0 {
        return false
    }

    for k, _ := range dict {
        if !strings.EqualFold(string(k), string(k)) {
            return false
        }
    }
    return true
}



