    vowels := "aeiouAEIOU"
    result := make([]rune, 0)

    for _, c := range message {
        if strings.ContainsRune(vowels, c) {
            result = append(result, rune(c)+2)
        } else if c >= 'a' && c <= 'z' {
            result = append(result, rune(c)-32)
        } else if c >= 'A' && c <= 'Z' {
            result = append(result, rune(c)+32)
        } else {
            result = append(result, c)
        }
    }

    return string(result)
}



