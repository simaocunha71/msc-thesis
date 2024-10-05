    alphabet := "abcdefghijklmnopqrstuvwxyz"
    return strings.Map(func(r rune) rune {
        index := strings.IndexRune(alphabet, r)
        if index < 0 {
            return r
        }
        newIndex := (index + 4) % len(alphabet)
        return alphabet[newIndex]
    }, s)
}



