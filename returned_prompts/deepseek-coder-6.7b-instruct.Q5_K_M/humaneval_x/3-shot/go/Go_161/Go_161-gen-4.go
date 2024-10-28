    hasLetters := false
    var result string
    for _, c := range s {
        if 'a' <= c && c <= 'z' || 'A' <= c && c <= 'Z' {
            hasLetters = true
            if 'a' <= c && c <= 'z' {
                result += strings.ToUpper(string(c))
            } else {
                result += strings.ToLower(string(c))
            }
        } else {
            result += string(c)
        }
    }
    if !hasLetters {
        return reverse(s)
    }
    return result
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



