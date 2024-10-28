```go
func F(n int) []int {
    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i%2 == 0 {
            factorial := 1
            for j := 1; j <= i+1; j++ {
                factorial *= j
            }
            result[i] = factorial
        } else {
            sum := 0
            for j := 1; j <= i+1; j++ {
                sum += j
            }
            result[i] = sum
        }
    }
    return result
}
```