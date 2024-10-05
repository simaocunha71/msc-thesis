```go
func Encrypt(s string) string {
    alphabet := "abcdefghijklmnopqrstuvwxyz"
    shiftedAlphabet := alphabet[2:] + alphabet[:2]
    encrypted := ""
    for _, r := range s {
        if strings.ContainsRune(alphabet, r) {
            index := strings.IndexRune(alphabet, r)
            encrypted += string(shiftedAlphabet[index])
        } else {
            encrypted += string(r)
        }
    }
    return encrypted
}
```
