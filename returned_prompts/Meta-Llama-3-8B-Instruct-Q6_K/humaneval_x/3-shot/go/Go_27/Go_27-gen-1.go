    return strings.Map(func(r rune) rune {
        if r == ' ' {
            return r
        }
        if unicode.IsLower(r) {
            return unicode.ToUpper(r)
        }
        if unicode.IsUpper(r) {
            return unicode.ToLower(r)
        }
        return r
    }, str)
}