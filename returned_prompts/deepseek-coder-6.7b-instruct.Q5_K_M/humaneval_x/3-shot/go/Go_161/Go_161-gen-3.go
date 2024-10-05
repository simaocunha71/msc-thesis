    result := []rune(s)
    for i := range result {
        if unicode.IsLetter(result[i]) {
            if unicode.IsLower(result[i]) {
                result[i] = unicode.ToUpper(result[i])
            } else {
                result[i] = unicode.ToLower(result[i])
            }
        }
    }
    return string(result)
}



