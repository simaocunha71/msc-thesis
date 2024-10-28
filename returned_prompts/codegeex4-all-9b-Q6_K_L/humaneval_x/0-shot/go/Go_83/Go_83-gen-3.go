```go
func StartsOneEnds(n int) int {
    if n == 1 {
        return 2
    }
    return int(math.Pow(9, float64(n-2)))*2 + StartsOneEnds(n-1)
}
```