```go
func StringSequence(n int) string {
    if n < 0 {
        return ""
    }
    var sb strings.Builder
    for i := 0; i <= n; i++ {
        sb.WriteString(strconv.Itoa(i))
        sb.WriteString(" ")
    }
    return strings.TrimSpace(sb.String())
}
```