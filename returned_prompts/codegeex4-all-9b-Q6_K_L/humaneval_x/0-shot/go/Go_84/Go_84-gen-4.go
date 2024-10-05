```go
func Solve(N int) string {
    sum := 0
    for ; N > 0; N /= 2 {
        sum += N % 2
    }
    return strconv.Itoa(sum)
}
```