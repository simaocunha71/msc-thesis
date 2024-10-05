    return strings.Map(func (c rune) rune {
        if c >= 'a' && c <= 'z' {
            return (c - 'a' + 4) % 26 + 'a'
        } else if c >= 'A' && c <= 'Z' {
            return (c - 'A' + 4) % 26 + 'A'
        } else {
            return c
        }
    }, s)
}

