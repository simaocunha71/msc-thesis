```go
func StringSequence(n int) string {
    var result string
    for i := 0; i <= n; i++ {
        result += strconv.Itoa(i) + " "
    }
    return result[:len(result)-1] // remove the last space
}
```