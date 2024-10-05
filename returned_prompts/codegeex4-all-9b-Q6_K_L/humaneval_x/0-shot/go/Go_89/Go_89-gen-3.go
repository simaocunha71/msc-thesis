```go
func Encrypt(s string) string {
    alphabet := "abcdefghijklmnopqrstuvwxyz"
    encrypted := ""
    for _, c := range s {
        if strings.ContainsRune(alphabet, c) {
            index := strings.IndexRune(alphabet, c)
            encrypted += string(alphabet[(index+4)%26])
        } else {
            encrypted += string(c)
        }
    }
    return encrypted
}
```
