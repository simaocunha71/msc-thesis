```go
func Encode(message string) string {
    result := make([]rune, 0, len(message))
    for _, c := range message {
        if strings.ContainsRune("AEIOUaeiou", c) {
            result = append(result, rune((c-'A'+2)%26+'A'))
        } else if strings.ContainsRune("aeiou", c) {
            result = append(result, rune((c-'a'+2)%26+'a'))
        } else {
            if 'a' <= c && c <= 'z' {
                result = append(result, c - 'a' + 'A')
            } else {
                result = append(result, c + 'a' - 'A')
            }
        }
    }
    return string(result)
}
```