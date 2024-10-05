```go
func StringSequence(n int) string {
    s := make([]string, n+1)
    for i := 0; i <= n; i++ {
        s[i] = strconv.Itoa(i)
    }
    return strings.Join(s, " ")
}
```