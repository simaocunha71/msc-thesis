    result := []rune(s)
    for i := 0; i < len(s); i++ {
        if unicode.IsLetter(rune(s[i])) {
            if unicode.IsUpper(rune(s[i])) {
                result[i] = unicode.ToLower(rune(s[i]))
            } else {
                result[i] = unicode.ToUpper(rune(s[i]))
            }
        }
    }
    return string(result)
}



