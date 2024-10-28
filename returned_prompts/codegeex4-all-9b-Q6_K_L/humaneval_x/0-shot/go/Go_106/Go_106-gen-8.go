
```go
func F(n int) []int {
    result := make([]int, n)
    for i := 1; i <= n; i++ {
        if i%2 == 0 {
            factorial := 1
            for j := 1; j <= i; j++ {
                factorial *= j
            }
            result[i-1] = factorial
        } else {
            sum := 0
            for j := 1; j <= i; j++ {
                sum += j
            }
            result[i-1] = sum
        }
    }
    return result
}
```