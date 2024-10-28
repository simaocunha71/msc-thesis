```go
func Encode(message string) string {
    vowels := []string{"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    encoded := ""
    for _, char := range message {
        if strings.ContainsRune(strings.ToLower(string(char)), 'a') {
            encoded += strings.ToUpper(string(rune(char) + 2))
        } else if strings.ContainsRune(strings.ToLower(string(char)), 'e') {
            encoded += strings.ToUpper(string(rune(char) + 2))
        } else if strings.ContainsRune(strings.ToLower(string(char)), 'i') {
            encoded += strings.ToUpper(string(rune(char) + 2))
        } else if strings.ContainsRune(strings.ToLower(string(char)), 'o') {
            encoded += strings.ToUpper(string(rune(char) + 2))
        } else if strings.ContainsRune(strings.ToLower(string(char)), 'u') {
            encoded += strings.ToUpper(string(rune(char) + 2))
        } else {
            if char >= 'a' && char <= 'z' {
                encoded += strings.ToUpper(string(char))
            } else if char >= 'A' && char <= 'Z' {
                encoded += strings.ToLower(string(char))
            } else {
                encoded += string(char)
            }
        }
    }
    return encoded
}
```
This function works by iterating through each character in the message. If the character is a vowel, it swaps the case of the character and adds 2 to its ASCII value to encode it. If the character is not a vowel, it checks if the character is lowercase or uppercase and swaps the case accordingly. If the character is not a letter, it adds it as is to the encoded string. Finally, it returns the encoded string.