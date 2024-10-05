The current function uses the math package in Go to calculate the result, which may not be the most efficient way to solve the problem. Here's a more efficient solution to calculate the result using bit manipulation:

```go
func StartsOneEnds(n int) int {
    if n == 1 {
        return 1
    }
    return int(math.Pow(10, float64(n-1))) + int(math.Pow(10, float64(n)))
}
```

This function first checks if the input `n` is equal to 1. If it is, it returns 1 because there is only one 1-digit positive integer that starts or ends with 1. Otherwise, it calculates the result by adding the number of `n`-digit positive integers that start with 1 (`math.Pow(10, float64(n-1))`) to the number of `n`-digit positive integers that end with 1 (`math.Pow(10, float64(n))`).

To improve the performance of this function, you can use bit manipulation to calculate the result. Here's an example:

```go
func StartsOneEnds(n int) int {
    if n == 1 {
        return 1
    }
    return (1<<(n-1)) + (1<<n)
}
```

In this version of the function, we use the left shift operator (`<<`) to multiply the value of 1 by 2 raised to the power of `n-1` and `n`. The result is the same as the previous version of the function, but the calculation is faster because it uses bit manipulation instead of the `math.Pow` function.

Overall, using bit manipulation can significantly improve the performance of this function