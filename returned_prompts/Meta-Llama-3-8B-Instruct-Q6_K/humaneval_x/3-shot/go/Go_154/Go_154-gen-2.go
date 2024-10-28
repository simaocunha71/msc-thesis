    for i := 0; i < len(b); i++ {
        for j := i; j < len(b); j++ {
            if strings.Contains(a, b[j-i : len(b)]) {
                return true
            }
        }
    }
    return false
}