    vowels := []string{"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    var encoded_message string
    for _, c := range message {
        if strings.ContainsRune(strings.Join(vowels, ""), c) {
            if c == 'a' || c == 'A' {
                encoded_message = encoded_message + string(c - 32)
            } else {
                encoded_message = encoded_message + string(c - 33)
            }
        } else {
            encoded_message = encoded_message + strings.ToUpper(string(c))
        }
    }
    return encoded_message
}

