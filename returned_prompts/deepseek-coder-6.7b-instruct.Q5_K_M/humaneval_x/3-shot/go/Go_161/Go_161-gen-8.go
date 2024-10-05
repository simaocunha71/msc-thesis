    str := []rune(s)
    for i := 0; i < len(str); i++ {
        if unicode.IsLetter(str[i]) {
            if unicode.IsLower(str[i]) {
                str[i] = unicode.ToUpper(str[i])
            } else {
                str[i] = unicode.ToLower(str[i])
            }
        }
    }
    return string(str)
}



