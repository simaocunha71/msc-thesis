The correct solution is:

```go
func SumToN(n int) int {
    sum := 0
    for i := 1; i <= n; i++ {
        sum += i
    }
    return sum
}
```

This function uses a for loop to iterate from 1 to n, and for each iteration, it adds the current number to the sum. The sum is then returned at the end of the function. This solution is straightforward and easy to understand. It has a time complexity of O(n) and a space complexity of O(1), which means it is efficient for large inputs.