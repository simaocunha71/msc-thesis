    return strings.Map(func(r rune) rune {
        if r >= 'A' && r <= 'Z' {
            return r + 'a' - 'A'
        } else if r >= 'a' && r <= 'z' {
            return r + 'A' - 'a'
        }
        return r
    }, str)
}



