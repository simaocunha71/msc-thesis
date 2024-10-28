    for i := 0; i < len(b); i++ {
        if strings.Contains(a, b[i:]) && strings.Contains(a, b[:i]) {
            return true
        }
    }
    return false
}



