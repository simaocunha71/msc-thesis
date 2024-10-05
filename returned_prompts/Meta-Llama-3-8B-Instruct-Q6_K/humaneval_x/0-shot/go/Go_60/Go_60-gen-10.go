The solution to this problem is:

```go
func SumToN(n int) int {
    sum := 0
    for i := 1; i <= n; i++ {
        sum += i
    }
    return sum
}
```

Explanation:

The function `SumToN` takes an integer `n` as input and returns the sum of all integers from 1 to `n`.

The function uses a for loop to iterate from 1 to `n`, and in each iteration, it adds the current number to the `sum` variable.

Finally, the function returns the `sum` variable, which is the sum of all integers from 1 to `n`.