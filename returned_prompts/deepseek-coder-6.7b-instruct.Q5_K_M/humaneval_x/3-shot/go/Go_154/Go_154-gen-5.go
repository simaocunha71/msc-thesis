    if len(b)>len(a) {
        return false
    }
    for _, _ = range b {
        if strings.Contains(a, b) {
            return true
        }
        b = b[1:] + string(b[0])
    }
    return false
}



