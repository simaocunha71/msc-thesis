// returns encoded string by shifting every character by 21 in the alphabet.
func EncodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch+21-'a')%26+'a')
    }
    return string(newRunes)
}

// takes as input string encoded with EncodeShift function. Returns decoded string.
func DecodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-21+26)%26+'a')
    }
    return string(newRunes)
}
