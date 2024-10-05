```go
func Digits(n int) int {
    product := 1
    for n > 0 {
        digit := n % 10
        if digit%2 == 1 {
            product *= digit
        }
        n /= 10
    }
    return product
}
```
