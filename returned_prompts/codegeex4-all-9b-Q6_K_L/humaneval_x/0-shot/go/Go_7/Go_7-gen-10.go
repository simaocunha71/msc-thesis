```go
func FilterBySubstring(stringList []string, substring string) []string {
    var res []string
    for _, s := range stringList {
        if strings.Contains(s, substring) {
            res = append(res, s)
        }
    }
    return res
}
```
