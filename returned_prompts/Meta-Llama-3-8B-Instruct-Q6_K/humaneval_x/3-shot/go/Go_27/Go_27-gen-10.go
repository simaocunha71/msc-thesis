    result := make([]rune, 0, len(str))
    for _, c := range str {
        if unicode.IsLower(c) {
            result = append(result, unicode.ToTitle(c))
        } else if unicode.IsUpper(c) {
            result = append(result, unicode.ToLower(c))
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}