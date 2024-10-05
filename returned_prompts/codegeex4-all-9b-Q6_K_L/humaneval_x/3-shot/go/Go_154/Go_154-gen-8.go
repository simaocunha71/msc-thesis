    for i := 0; i < len(a); i++ {
        if a[i:] + a[:i] == b {
            return true
        }
    }
    return false
}



