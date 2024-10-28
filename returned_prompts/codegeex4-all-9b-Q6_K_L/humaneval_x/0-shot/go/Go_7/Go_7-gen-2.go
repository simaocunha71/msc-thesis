```go
func FilterBySubstring(stringList []string, substring string) []string {
    var filteredList []string
    for _, s := range stringList {
        if strings.Contains(s, substring) {
            filteredList = append(filteredList, s)
        }
    }
    return filteredList
}
```