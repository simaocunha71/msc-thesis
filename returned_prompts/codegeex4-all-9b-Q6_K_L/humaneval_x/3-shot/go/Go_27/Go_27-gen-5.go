    return strings.Map(func(r rune) rune{
        if r >= 'a' && r <= 'z' {
            return r - 'a' + 'A'
        } else if r >= 'A' && r <= 'Z' {
            return r - 'A' + 'a'
        } else {
            return r
        }
    }, str)
}

