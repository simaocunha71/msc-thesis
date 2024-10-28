```go
func CheckIfLastCharIsALetter(txt string) bool {
    if strings.TrimSpace(txt) == "" {
        return false
    }
    lastChar := txt[len(txt)-1]
    return (lastChar >= 'A' && lastChar <= 'Z') || (lastChar >= 'a' && lastChar <= 'z')
}
```
