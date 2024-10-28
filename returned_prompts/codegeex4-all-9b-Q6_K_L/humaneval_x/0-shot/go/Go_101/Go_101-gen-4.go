```go
func WordsString(s string) []string {
    var out []string
    for _, word := range strings.Fields(s) {
        out = append(out, strings.Split(word, ",")...)
    }
    return out
}
```
