```go
func Encode(message string) string {
    vowels := "aeiou"
    encoded := ""
    for _, c := range message {
        if strings.ContainsRune(vowels, c) {
            encoded += string(c + 2)
        } else if c >= 'a' && c <= 'z' {
            encoded += string(c - 32)
        } else if c >= 'A' && c <= 'Z' {
            encoded += string(c + 32)
        } else {
            encoded += string(c)
        }
    }
    return encoded
}
```