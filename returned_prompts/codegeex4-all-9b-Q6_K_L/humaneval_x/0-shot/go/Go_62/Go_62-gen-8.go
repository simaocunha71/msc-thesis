```go
func Derivative(xs []int) []int {
    if len(xs) <= 1 {
        return []int{}
    }
    result := make([]int, len(xs)-1)
    for i := 1; i < len(xs); i++ {
        result[i-1] = xs[i] * i
    }
    return result
}
```
