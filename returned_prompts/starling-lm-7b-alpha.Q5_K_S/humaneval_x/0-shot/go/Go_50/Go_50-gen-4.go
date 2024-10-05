    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, ((ch-5)%26+'a'))
    }
    return string(newRunes)
}

// Encoding and Decoding by shifting characters in the alphabet
// takes as input string and returns encoded string by shifting every character by 5 in the alphabet.
func EncodeCaesarCipher(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        if 'a' <= ch && ch <= 'z' {
            newRunes = append(newRunes, (ch+5-'a')%26+'a')
        } else if 'A' <= ch && ch <= 'Z' {
            newRunes = append(newRunes, (ch+5-'A')%26+'A')
        } else {
            newRunes = append(newRunes, ch)
        }
    }
    return string(newRunes)
}

// takes as input encoded string and returns decoded string.
func DecodeCaesarCipher(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        if 'a' <= ch && ch <= 'z' {
            newRunes = append(newRunes, ((ch-5)%26+'a'))
        } else if 'A' <= ch && ch <= 'Z' {
            newRunes = append(newRunes, ((ch-5)%26+'A'))
        } else {
            newRunes = append(newRunes, ch)
        }
    }
    return string(newRunes)
}























































