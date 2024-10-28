```go
func FixSpaces(text string) string {
    return strings.ReplaceAll(strings.ReplaceAll(text, "  ", "-"), " ", "_")
}
```
