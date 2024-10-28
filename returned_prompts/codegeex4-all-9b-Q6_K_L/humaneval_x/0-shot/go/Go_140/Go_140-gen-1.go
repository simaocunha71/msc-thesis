Here is the solution in Go:

```go
func FixSpaces(text string) string {
    text = strings.Replace(text, "  ", "-", -1) // Replace two consecutive spaces with a dash
    text = strings.Replace(text, " ", "_", -1)  // Replace all remaining spaces with an underscore
    return text
}
```
This solution first replaces all two consecutive spaces with a dash, and then replaces all remaining spaces with an underscore.