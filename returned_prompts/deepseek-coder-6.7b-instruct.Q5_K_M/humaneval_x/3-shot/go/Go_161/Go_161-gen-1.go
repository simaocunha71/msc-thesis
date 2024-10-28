    result := []rune(s)
    for i, c := range s {
        if unicode.IsLetter(c) {
            if unicode.IsLower(c) {
                result[i] = unicode.ToUpper(c)
            } else {
                result[i] = unicode.ToLower(c)
            }
        }
    }

    if strings.ContainsAny(s, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return string(result)
    } else {
        return reverse(s)
    }
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



