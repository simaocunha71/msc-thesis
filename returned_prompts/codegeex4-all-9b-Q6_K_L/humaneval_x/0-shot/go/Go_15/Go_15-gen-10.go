```go
func StringSequence(n int) string {
    var builder strings.Builder
    for i := 0; i <= n; i++ {
        builder.WriteString(strconv.Itoa(i))
        if i < n {
            builder.WriteString(" ")
        }
    }
    return builder.String()
}
```
