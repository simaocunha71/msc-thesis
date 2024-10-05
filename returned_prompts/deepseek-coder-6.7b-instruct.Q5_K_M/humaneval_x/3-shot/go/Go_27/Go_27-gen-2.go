    var result string
    for _, c := range str {
        if c >= 'a' && c <= 'z' {
            result += strings.ToUpper(string(c))
        } else if c >= 'A' && c <= 'Z' {
            result += strings.ToLower(string(c))
        } else {
            result += string(c)
        }
    }
    return result
}



