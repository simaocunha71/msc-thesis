    for i := 0; i < len(b); i++ {
        b_rotated := b[i:] + b[:i]
        if strings.Contains(a, b_rotated) {
            return true
        }
    }
    return false
}