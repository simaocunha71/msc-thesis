You can use the modulo operator to check if a number divides evenly into n. Here's a simple implementation in Go:

```go
func LargestDivisor(n int) int {
    for i := n - 1; i > 0; i-- {
        if n % i == 0 {
            return i
        }
    }
    return n
}
```

This function starts at n - 1 and decrements until it finds a number that divides n evenly. If no such number is found, it returns n.