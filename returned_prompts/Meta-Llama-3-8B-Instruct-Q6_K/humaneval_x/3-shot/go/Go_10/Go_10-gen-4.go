    runes := []rune(str)
    i := len(runes) - 1
    for i > 0 {
        if runes[i-1] != runes[i] {
            i--
        } else {
            i--
        }
    }
    return string(runes[:i+1]) + string(reverse(runes[i:]))
}

func reverse(s []rune) []rune {
    r := []rune(s[:0])
    copy(r, s)
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    return r
}