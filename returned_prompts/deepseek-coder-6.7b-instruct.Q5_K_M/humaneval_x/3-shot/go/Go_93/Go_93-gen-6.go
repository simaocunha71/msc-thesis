    vowels := "aeiouAEIOU"
    alphabet := "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encoded := ""

    for _, char := range message {
        if strings.ContainsRune(vowels, char) {
            encoded += string(alphabet[strings.Index(alphabet, string(char))+2])
        } else {
            encoded += string(char)
        }
    }

    return encoded
}



