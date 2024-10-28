    for i := 0; i < len(b); i++ {
        if strings.Contains(a, b[i : len(b)]) {
            return true
        }
    }
    return false
}