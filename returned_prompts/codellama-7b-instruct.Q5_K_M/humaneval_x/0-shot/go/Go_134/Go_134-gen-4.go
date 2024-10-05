    return strings.LastIndexFunc(txt, func(r rune) bool {
        return unicode.IsLetter(r)
    }) == len(txt)-1
}
