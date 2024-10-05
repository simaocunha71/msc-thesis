    return strings.Map(func(r rune) rune {
        if r >= 'a' && r <= 'z' {
            return 'a' + ((r-'a')*2+26)%26
        }
        if r >= 'A' && r <= 'Z' {
            return 'A' + ((r-'A')*2+26)%26
        }
        return r
    }, s)
}

