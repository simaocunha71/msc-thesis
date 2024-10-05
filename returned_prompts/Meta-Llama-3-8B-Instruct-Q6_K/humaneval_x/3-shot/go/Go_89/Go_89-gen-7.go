    alphabet := "abcdefghijklmnopqrstuvwxyz"
    encrypted := strings.Map(func(r rune) rune {
        if r >= 'a' && r <= 'z' {
            idx := int(r - 'a')
            idx = (idx + 4 * 2) % 26
            return rune('a' + idx)
        }
        return r
    }, s)
    return string(encrypted)
}