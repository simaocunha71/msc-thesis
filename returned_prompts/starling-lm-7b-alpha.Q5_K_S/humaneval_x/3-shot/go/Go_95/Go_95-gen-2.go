    for k, _ := range dict {
        if k != "" && (k[0] >= 'A' && k[0] <= 'Z' || k[0] >= 'a' && k[0] <= 'z') {
            return false
        }
    }
    return true
}



