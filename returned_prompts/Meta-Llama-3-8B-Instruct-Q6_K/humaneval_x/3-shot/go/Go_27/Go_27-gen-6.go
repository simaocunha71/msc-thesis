    return strings.Map(func(r rune) rune {
        if unicode.IsLower(r) {
            return unicode.ToUpper(r)
        } else if unicode.IsUpper(r) {
            return unicode.ToLower(r)
        }
        return r
    }, str)
}