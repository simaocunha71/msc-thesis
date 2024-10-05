    result := ""
    for _, c := range s {
        if unicode.IsLetter(c) {
            if unicode.IsUpper(c) {
                result += string(unicode.ToLower(c))
            } else {
                result += string(unicode.ToUpper(c))
            }
        } else {
            result += string(c)
        }
    }
    return result
}