The function `SumToN` takes an integer `n` as input and returns the sum of all integers from 1 to `n`. Here's the implementation in Go:

```go
func SumToN(n int) int {
    sum := 0
    for i := 1; i <= n; i++ {
        sum += i
    }
    return sum
}
```

This function uses a for loop to iterate from 1 to `n`, adding each number to a running total. The final total is returned as the result. For example, `SumToN(30)` returns `465`, which is the sum of the numbers from 1 to 30. Similarly, `SumToN(100)` returns `5050`, which is the sum of the numbers from 1 to 100.