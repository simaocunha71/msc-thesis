    bLen := len(b)
    for i := 0; i < len(a); i++ {
        if a[i:i+bLen] == b {
            return true
        }
        if i+bLen <= len(a) {
            b = b[1:] + b[0]
        }
    }
    return false
}