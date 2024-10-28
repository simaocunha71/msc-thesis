```go
func F(n int) []int {
    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i%2 == 0 {
            result[i] = factorial(i)
        } else {
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
    if n == 0 {
        return 1
    }
    return n * factorial(n-1)
}
```
In this solution, we first create a slice of size `n` to store the result. Then, we iterate over the slice. For each element, if the index is even, we calculate the factorial of the index using a helper function `factorial`. If the index is odd, we calculate the sum of numbers from 1 to `i`. Finally, we return the result slice.

The `factorial` function is a recursive function that calculates the factorial of a given number `n`. It returns 1 if `n` is 0, and `n` times the factorial of `n-1` otherwise. This function is used to calculate the factorial of even indices in the result slice.