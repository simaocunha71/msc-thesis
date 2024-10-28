```go
func StringSequence(n int) string {
    var sb strings.Builder
    for i := 0; i <= n; i++ {
        sb.WriteString(strconv.Itoa(i))
        if i < n {
            sb.WriteString(" ")
        }
    }
    return sb.String()
}
```