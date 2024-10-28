The function LargestDivisor(n int) int takes an integer n as input and returns the largest number that divides n evenly, smaller than n.

Here's a sample implementation in Go:

```go
func LargestDivisor(n int) int {
    for i := n / 2; i > 0; i-- {
        if n % i == 0 {
            return i
        }
    }
    return 1
}
```

This function works by iterating from `n/2` down to 1, checking if `n` is divisible by each number. The first number it finds that `n` is divisible by is the largest divisor less than `n`. If no such number is found, the function returns 1, which is the only number that divides 0 evenly.