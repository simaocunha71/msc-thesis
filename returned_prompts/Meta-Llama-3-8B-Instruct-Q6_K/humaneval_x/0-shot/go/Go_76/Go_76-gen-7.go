```
func IsSimplePower(x int, n int) bool {
    // Check if the base is 1
    if n == 1 {
        return true
    }
    // Check if the number is a power of n
    for i := 1; x > 1; i++ {
        if math.Pow(float64(n), float64(i)) == float64(x) {
            return true
        }
    }
    return false
}
```


This function uses a loop to check if x is a power of n. If n is 1, the function immediately returns true because any number is a power of 1. Otherwise, the function checks if x is equal to n raised to the power of i, starting from i = 1. If it finds a match, it returns true. If it doesn't find a match after checking all possible values of i, it returns false. The function uses the math.Pow function to calculate the power of n. The loop continues until x is less than or equal to 1, at which point it returns false. The function is case-sensitive and will return false if the input numbers are negative. 

The time complexity of this function is O(log(x)) because the function checks up to log(x) possible values of i. The space complexity is O(1) because the function uses a constant amount of space to store the variables and loop counter. 

This function can be optimized by using a logarithmic search instead of a linear search. This would reduce the time complexity to O(log(log(x))). However, the logarithmic search would be more complex to implement and may not be worth the small improvement in performance for most use cases. 

The function can also be optimized by using a more efficient method to check if x is a power of n, such as using the fact that if x is a power of n, then the logarithm of x to the base n is an integer. However, this would also make the function more complex and may not be worth the small improvement in performance for most use cases. 

In general, the provided function is a simple and efficient solution that is easy to understand and implement. It is suitable for most use cases and can be used as-is. 

Here is the optimized version of the function using a logarithmic search:

```go
func IsSimplePower(x int, n int) bool {
    if n == 1 {
        return true
    }
    i := 0
    for x > 1