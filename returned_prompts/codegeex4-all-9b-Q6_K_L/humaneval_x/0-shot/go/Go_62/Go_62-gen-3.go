```go
func Derivative(xs []int) []int {
    if len(xs) == 0 {
        return []int{}
    }
    derivative := make([]int, len(xs)-1)
    for i := 1; i < len(xs); i++ {
        derivative[i-1] = xs[i] * i
    }
    return derivative
}
```
