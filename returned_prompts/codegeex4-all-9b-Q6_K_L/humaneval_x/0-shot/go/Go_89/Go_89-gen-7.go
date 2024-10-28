```go
func Encrypt(s string) string {
    alphabet := "abcdefghijklmnopqrstuvwxyz"
    shift := 4
    encrypted := ""
    for _, c := range s {
        if strings.ContainsRune(alphabet, c) {
            index := strings.IndexRune(alphabet, c)
            new_index := (index + shift) % len(alphabet)
            encrypted += string(alphabet[new_index])
        } else {
            encrypted += string(c)
        }
    }
    return encrypted
}
```