    rotated_alphabet := strings.Map(func(r rune) rune {
        switch {
            case r >= 'a' && r <= 'z': return r + 2 * 2
            case r >= 'A' && r <= 'Z': return r + 2 * 2
        }
        return r
    }, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return strings.Map(func(r rune) rune {
        for i, v := range rotated_alphabet {
            if r == v {
                return rune(i)
            }
        }
        return r
    }, s)
}



