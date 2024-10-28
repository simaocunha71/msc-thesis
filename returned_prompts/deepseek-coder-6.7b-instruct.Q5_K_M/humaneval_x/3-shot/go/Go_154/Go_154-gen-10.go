    for _, _ = range b {
        if strings.Contains(a, b) {
            return true
        }
        b = b[len(b)-1:] + b[:len(b)-1]
    }
    return false
}



