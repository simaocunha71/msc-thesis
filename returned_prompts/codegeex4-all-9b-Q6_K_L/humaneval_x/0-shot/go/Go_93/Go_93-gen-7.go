```go
func Encode(message string) string {
    vowels := []string{"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    encoded := ""
    for _, char := range message {
        if strings.ContainsRune(strings.ToLower(string(char)), 'a') || strings.ContainsRune(strings.ToLower(string(char)), 'e') || strings.ContainsRune(strings.ToLower(string(char)), 'i') || strings.ContainsRune(strings.ToLower(string(char)), 'o') || strings.ContainsRune(strings.ToLower(string(char)), 'u') {
            if strings.ToLower(string(char)) == "a" {
                encoded += string('c')
            } else if strings.ToLower(string(char)) == "e" {
                encoded += string('g')
            } else if strings.ToLower(string(char)) == "i" {
                encoded += string('k')
            } else if strings.ToLower(string(char)) == "o" {
                encoded += string('q')
            } else if strings.ToLower(string(char)) == "u" {
                encoded += string('s')
            }
        } else if strings.ToLower(string(char)) == "A" {
            encoded += string('C')
        } else if strings.ToLower(string(char)) == "E" {
            encoded += string('G')
        } else if strings.ToLower(string(char)) == "I" {
            encoded += string('K')
        } else if strings.ToLower(string(char)) == "O" {
            encoded += string('Q')
        } else if strings.ToLower(string(char)) == "U" {
            encoded += string('S')
        } else {
            if char >= 65 && char <= 90 {
                encoded += string(char + 32)
            } else {
                encoded += string(char - 32)
            }
        }
    }
    return encoded
}
```