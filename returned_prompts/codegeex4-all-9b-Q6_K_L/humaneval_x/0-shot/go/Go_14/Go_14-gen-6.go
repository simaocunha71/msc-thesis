```go
func AllPrefixes(str string) []string {
    var allPrefixes []string
    for i := 1; i <= len(str); i++ {
        allPrefixes = append(allPrefixes, str[:i])
    }
    return allPrefixes
}
```
