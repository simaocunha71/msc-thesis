    for i := 0; i < len(b); i++ {
        b_rot := b[i:] + b[:i]
        if strings.Contains(a, b_rot) {
            return true
        }
    }
    return false
}
}