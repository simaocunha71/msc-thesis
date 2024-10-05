    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-5+26)%26+'a')
    }
    return string(newRunes)
}

// Encodes the string by replacing each character by the character with the same ASCII code 5 positions ahead.
func EncodeASCII(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, ch+5)
    }
    return string(newRunes)
}

// Decodes the string by replacing each character by the character with the same ASCII code 5 positions behind.
func DecodeASCII(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, ch-5)
    }
    return string(newRunes)
}




// Encodes the string by replacing each character by its Unicode code point 5 positions ahead.
func EncodeUnicode(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, ch+5)
    }
    return string(newRunes)
}

// Decodes the string by replacing each character by its Unicode code point 5 positions behind.
func DecodeUnicode(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, ch-5)
    }
    return string(newRunes)
}
































