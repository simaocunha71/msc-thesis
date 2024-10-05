    result := ""
    for _, ch := range str {
        if ch >= 'a' && ch <= 'z' {
            result += strings.ToUpper(string(ch))
        } else if ch >= 'A' && ch <= 'Z' {
            result += strings.ToLower(string(ch))
        } else {
            result += string(ch)
        }
    }
    return result
}



