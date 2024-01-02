// returns encoded string by shifting every character by 5 in the alphabet.
func EncodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch+5-'a')%26+'a')
    }
    return string(runes)
}

// takes as input string encoded with EncodeShift function. Returns decoded string.
func DecodeShift(s string) string {
    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-'a'+5)%26+49+'a')
    }
    return string(runes[1:])
}

// Example of use. Encodes "hello" and then decodes it back to the original string.
func main() {
    encode := EncodeShift("hello")
    println(DecodeShift(encode))
}
