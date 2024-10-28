    if len(a) < len(b) {
        return false
    }
    for i := 0; i < len(b); i++ {
        if strings.Contains(a, b) {
            return true
        }
        b = b[len(b)-1:] + b[:len(b)-1]
    }
    return false
}



