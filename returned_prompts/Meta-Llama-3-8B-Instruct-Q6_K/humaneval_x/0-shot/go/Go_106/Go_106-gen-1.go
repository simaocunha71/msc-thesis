Here is a simple implementation of the function F in Go:

```go
func F(n int) []int {
    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i % 2 == 0 { // i is even
            result[i] = factorial(i)
        } else { // i is odd
            sum := 0
            for j := 1; j <= i; j++ {
                sum += j
            }
            result[i] = sum
        }
    }
    return result
}

func factorial(n int) int {
    result := 1
    for i := 2; i <= n; i++ {
        result *= i
    }
    return result
}
```

In this function, we use a loop to iterate over the range from 0 to n-1. For each index i, we check if i is even or odd. If i is even, we calculate the factorial of i using the helper function factorial and assign it to the result slice. If i is odd, we calculate the sum of numbers from 1 to i using a nested loop and assign it to the result slice.

The helper function factorial calculates the factorial of a given number by multiplying all numbers from 1 to that number. It's a simple recursive function that multiplies the result with the current number until it reaches the given number. For example, factorial(5) would return 1 * 2 * 3 * 4 * 5 = 120.