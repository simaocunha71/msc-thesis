```go
func CheckIfLastCharIsALetter(txt string) bool {
    return len(txt) > 0 && !strings.HasSuffix(txt, " ") && txt[len(txt)-1] >= 'a' && txt[len(txt)-1] <= 'z' || txt[len(txt)-1] >= 'A' && txt[len(txt)-1] <= 'Z'
}
```
