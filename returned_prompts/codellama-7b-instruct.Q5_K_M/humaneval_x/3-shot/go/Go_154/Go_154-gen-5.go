    for i :=0; i<len(b); i++ {
        if strings.Contains(a, string(b[i])) {
            return true
        }
    }
    return false
}



