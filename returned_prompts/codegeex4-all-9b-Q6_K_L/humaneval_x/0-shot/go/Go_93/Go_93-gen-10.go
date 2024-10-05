```go
func Encode(message string) string {
    vowels := []string{"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    encoded := ""
    for _, c := range message {
        if strings.ContainsAny(string(c), "aeiouAEIOU") {
            encoded += string(c + 2)
        } else if strings.ContainsAny(string(c), "AEIOU") {
            encoded += strings.ToLower(string(c))
        } else if strings.ContainsAny(string(c), "aeiou") {
            encoded += strings.ToUpper(string(c))
        } else {
            encoded += string(c)
        }
    }
    return encoded
}
```