```go
func SpecialFactorial(n int) int {
    factorial := 1
    for i := n; i > 0; i-- {
        factorial *= i
    }
    return factorial
}
```
