You can solve this by using a simple loop that iterates from 1 to n and adds each number to a running total. Here's a simple implementation in Go:

```go
func SumToN(n int) int {
    sum := 0
    for i := 1; i <= n; i++ {
        sum += i
    }
    return sum
}
```

This function starts with a sum of 0 and then adds each number from 1 to n to the sum. Once the loop is finished, the function returns the final sum.