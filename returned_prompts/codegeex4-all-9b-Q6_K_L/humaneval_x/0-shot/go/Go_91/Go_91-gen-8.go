```go
func IsBored(S string) int {
    r := regexp.MustCompile(`I[^.?!]*[.?!]`)
    return len(r.FindAllString(S, -1))
}
```
