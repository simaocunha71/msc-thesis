Here is the solution in Go:

```go
func StartsOneEnds(n int) int {
    if n == 1 {
        return 2
    } else if n == 2 {
        return 3
    } else {
        // Calculate the number of n-digit positive integers that start or end with 1.
        // This can be done by subtracting the number of n-digit positive integers that start or end with 0 from the total number of n-digit positive integers.
        return int(math.Pow(10, float64(n-1))) - 2*int(math.Pow(10, float64(n-2))) + StartsOneEnds(n-1)
    }
}
```
This function uses recursion to calculate the number of n-digit positive integers that start or end with 1. The base cases are when n is 1 or 2, where the function returns 2 and 3 respectively. For n greater than 2, the function first calculates the number of n-digit positive integers that start or end with 0 by subtracting the number of (n-1)-digit positive integers that start or end with 1 from the total number of n-digit positive integers. Then, it adds the number of (n-1)-digit positive integers that start or end with 1 to get the total number of n-digit positive integers that start or end with 1.