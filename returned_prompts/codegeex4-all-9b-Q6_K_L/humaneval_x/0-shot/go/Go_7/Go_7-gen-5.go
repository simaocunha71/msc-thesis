```go
func FilterBySubstring(stringList []string, substring string) []string {
    var out []string
    for _, s := range stringList {
        if strings.Contains(s, substring) {
            out = append(out, s)
        }
    }
    return out
}
```