    for i := range b {
        if strings.Contains(a, b) {
            return true
        }
        b = b[1:] + string(b[0])
    }
    return false
}



