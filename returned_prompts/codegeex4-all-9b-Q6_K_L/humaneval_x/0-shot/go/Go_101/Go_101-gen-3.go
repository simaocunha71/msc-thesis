```go
func WordsString(s string) []string {
    return strings.FieldsFunc(s, func(r rune) bool {
        return r == ',' || r == ' '
    })
}
```