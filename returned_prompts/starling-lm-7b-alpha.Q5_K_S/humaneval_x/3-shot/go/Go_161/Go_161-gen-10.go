    result := make([]rune, len(s))
    for i, c := range s {
        if unicode.IsLetter(c) {
            result[i] = unicode.ToUpper(c) ^ unicode.ToLower(c)
        }else {
            result[i] = c
        }
    }
    return string(result)
}



