    vowels := "aeiouAEIOU"
    new_message := ""
    for _, c := range message {
        if strings.ContainsRune(vowels, c) {
            switch {
            case 'a' <= c && c <= 'z':
                new_message += string(c + 2)
            case 'A' <= c && c <= 'Z':
                new_message += string(c + 2)
            }
        } else {
            if 'a' <= c && c <= 'z' {
                new_message += strings.ToUpper(string(c))
            } else {
                new_message += strings.ToLower(string(c))
            }
        }
    }
    return new_message
}



