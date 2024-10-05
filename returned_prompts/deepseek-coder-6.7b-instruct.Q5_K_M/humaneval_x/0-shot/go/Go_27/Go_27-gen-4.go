    return strings.Map(func(r rune) rune {
        if unicode.Is(unicode.Ll, r) {
            return unicode.ToUpper(r)
        } else if unicode.Is(unicode.Lu, r) {
            return unicode.