    result := ""
    for _, c := range str {
        if strings.ToLower(string(c)) == string(c) {
            result += strings.ToUpper(string(c))
        } else {
            result += strings.ToLower(string(c))
        }
    }
    return result
} 