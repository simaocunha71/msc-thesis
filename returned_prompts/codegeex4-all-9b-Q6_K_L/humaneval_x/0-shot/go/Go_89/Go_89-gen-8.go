```go
func Encrypt(s string) string {
    s = strings.ToLower(s)
    encrypted := ""
    for _, char := range s {
        if char >= 'a' && char <= 'z' {
            encrypted += string((char-'a'+4)%26 + 'a')
        } else {
            encrypted += string(char)
        }
    }
    return encrypted
}
```
