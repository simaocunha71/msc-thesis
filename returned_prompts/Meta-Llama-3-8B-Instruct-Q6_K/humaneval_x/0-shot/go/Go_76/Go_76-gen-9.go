```
func IsSimplePower(x int, n int) bool {
    if x < 1 {
        return false
    }
    for i := 1; math.Pow(float64(n), float64(i)) <= float64(x); i++ {
        if math.Pow(float64(n), float64(i)) == float64(x) {
            return true
        }
    }
    return false
}
```


The code above defines a function `IsSimplePower` that takes two integers `x` and `n` as input and returns a boolean value indicating whether `x` is a simple power of `n` or not.

The function first checks if `x` is less than 1. If it is, the function immediately returns `false`, since `x` cannot be a simple power of `n` if it is less than 1.

Then, the function enters a loop that increments the power `i` of `n` until the power of `n` is greater than `x`. Inside the loop, the function checks if the power of `n` is equal to `x`. If it is, the function returns `true`, indicating that `x` is a simple power of `n`.

If the loop completes without finding a match, the function returns `false`, indicating that `x` is not a simple power of `n`. This is because the loop checks all possible powers of `n` up to and including the square root of `x`, so if `x` is not a simple power of `n`, it must be greater than the square of `n`.

The `math.Pow` function is used to calculate the power of `n` to the power of `i`. The `float64` conversions are used to ensure that the calculation is done in floating-point arithmetic, which is more accurate than integer arithmetic for large values of `x` and `n`.