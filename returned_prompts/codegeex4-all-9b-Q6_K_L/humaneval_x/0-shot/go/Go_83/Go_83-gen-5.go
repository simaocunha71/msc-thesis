```go
func StartsOneEnds(n int) int {
    if n <= 0 {
        return 0
    }
    if n == 1 {
        return 2
    }
    return 9*(int(math.Pow(10, float64(n-2)))) + StartsOneEnds(n-2)
}
```