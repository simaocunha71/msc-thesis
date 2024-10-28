    result := make([]rune, 0)
    for _, c := range message {
        if strings.Contains("aeiou", strings.ToLower(string(c))) {
            result = append(result, rune(c+2))
        } else {
            result = append(result, strings.ToLower(string(c)))
        }
    }
    return strings.ToUpper(string(result))
}

