```go
func CheckIfLastCharIsALetter(txt string) bool {
    if len(txt) == 0 {
        return false
    }
    lastChar := txt[len(txt)-1]
    if (lastChar >= 'a' && lastChar <= 'z') || (lastChar >= 'A' && lastChar <= 'Z') {
        return !strings.HasSuffix(txt, " ")
    }
    return false
}
```
