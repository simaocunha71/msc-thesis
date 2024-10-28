    var result string

    for _, c := range message {
        if strings.Contains("aeiou", string(c)) {
            result += string(c)
            result += string(c+2)
        } else {
            result += strings.ToUpper(string(c))
            result += strings.ToLower(string(c))
        }
    }
    return result
}



