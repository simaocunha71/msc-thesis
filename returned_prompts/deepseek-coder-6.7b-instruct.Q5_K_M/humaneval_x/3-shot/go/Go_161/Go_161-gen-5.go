    hasLetter := false
    out := []rune(s)
    for i, c := range out {
        if unicode.IsLetter(c) {
            hasLetter = true
            if unicode.IsLower(c) {
                out[i] = unicode.ToUpper(c)
            } else {
                out[i] = unicode.ToLower(c)
            }
        }
    }
    if !hasLetter {
        return reverse(s)
    }
    return string(out)
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}


