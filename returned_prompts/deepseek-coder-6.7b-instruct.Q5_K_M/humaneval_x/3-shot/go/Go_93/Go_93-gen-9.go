    vowels := "aeiou"
    alphabet := "abcdefghijklmnopqrstuvwxyz"
    ALPHABET := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encodedMessage := ""

    for _, char := range message {
        if strings.ContainsRune(vowels, char) {
            encodedMessage += string(ALPHABET[((strings.IndexRune(alphabet, char)+2)%26)])
        } else if strings.ContainsRune(ALPHABET, char) {
            encodedMessage += string(ALPHABET[((strings.IndexRune(alphabet, char)+2)%26)])
        } else {
            encodedMessage += string(char)
        }
    }

    return encodedMessage
}



