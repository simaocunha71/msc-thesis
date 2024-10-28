```go
func CheckIfLastCharIsALetter(txt string) bool {
    if len(txt) == 0 {
        return false
    }
    lastChar := txt[len(txt)-1]
    return lastChar >= 'a' && lastChar <= 'z' || lastChar >= 'A' && lastChar <= 'Z' && !strings.HasSuffix(txt, " ")
}
```
