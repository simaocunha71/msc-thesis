    result := ""
    for _, char := range str {
        if unicode.IsUpper(char) {
            result += strings.ToLower(string(char))
        } else {
            result += strings.ToUpper(string(char))
        }
    }
    return result
}



