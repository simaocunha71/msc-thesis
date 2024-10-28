```go
func FilterBySubstring(stringList []string, substring string) []string {
    returnFilter := []string{}
    for _, str := range stringList {
        if strings.Contains(str, substring) {
            returnFilter = append(returnFilter, str)
        }
    }
    return returnFilter
}
```
