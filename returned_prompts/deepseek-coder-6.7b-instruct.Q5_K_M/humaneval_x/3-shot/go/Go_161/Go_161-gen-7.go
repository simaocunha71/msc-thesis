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
    if strings.ContainsAny(s, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return string(result)
    } else {
        return reverse(string(result))
    }
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



