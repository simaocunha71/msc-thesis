    for i := 0; i < len(b); i++ {
        if strings.Contains(a, b) {
            return true
        }
        b = b[1:] + string(b[0])
    }
    return false
}



