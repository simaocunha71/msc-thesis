    var vowels = "AEIOUaeiou"
    var encoded_message string
    for _, c := range message {
        if strings.ContainsRune(vowels, c) {
            c = rune(c + 2)
        } else {
            c = rune(c ^ 32)
        }
        encoded_message += string(c)
    }
    return encoded_message
}

