```go
func Encode(message string) string {
    vowels := "aeiou"
    encoded := make([]rune, len(message))
    for i, c := range message {
        if strings.ContainsRune(vowels, c) {
            encoded[i] = c + 2
        } else if c >= 'a' && c <= 'z' {
            encoded[i] = c - 'a' + 'A'
        } else if c >= 'A' && c <= 'Z' {
            encoded[i] = c - 'A' + 'a'
        } else {
            encoded[i] = c
        }
    }
    return string(encoded)
}
```