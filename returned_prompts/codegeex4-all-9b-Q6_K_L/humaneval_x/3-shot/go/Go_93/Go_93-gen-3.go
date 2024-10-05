    vowels := "aeiouAEIOU"
    result := ""
    for _, c := range message {
        if strings.ContainsRune(vowels, c) {
            result += string(c + 2)
        } else {
            result += strings.ToLower(string(c))
        }
    }
    return result
}



