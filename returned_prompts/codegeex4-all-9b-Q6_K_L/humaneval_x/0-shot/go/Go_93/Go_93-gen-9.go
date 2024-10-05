```go
func Encode(message string) string {
    vowels := "AEIOUaeiou"
    encoded := ""
    for _, c := range message {
        if strings.ContainsRune(vowels, c) {
            encoded += string(rune((c - 'A' + 2) % 26 + 'A'))
        } else {
            if 'a' <= c && c <= 'z' {
                encoded += string(c - 'a' + 'A')
            } else {
                encoded += string(c - 'A' + 'a')
            }
        }
    }
    return encoded
}
```