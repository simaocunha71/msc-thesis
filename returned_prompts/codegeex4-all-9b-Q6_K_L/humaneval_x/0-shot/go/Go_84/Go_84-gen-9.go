```go
func Solve(N int) string {
    binary := strconv.FormatInt(int64(N), 2)
    sum := 0
    for _, digit := range binary {
        sum += int(digit - '0')
    }
    return strconv.Itoa(sum)
}
```