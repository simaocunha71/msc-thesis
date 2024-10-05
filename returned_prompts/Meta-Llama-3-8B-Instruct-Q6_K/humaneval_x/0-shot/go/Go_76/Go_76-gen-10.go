```
func IsSimplePower(x int, n int) bool {
    for i := 1; i <= x; i++ {
        if math.Pow(float64(n), float64(i)) == float64(x) {
            return true
        }
    }
    return false
}
```


Here is the explanation of the code:

The function `IsSimplePower(x int, n int)` takes two integers `x` and `n` as input. It returns `true` if `x` is a simple power of `n` and `false` otherwise.

The function uses a for loop to iterate from 1 to `x`. In each iteration, it calculates the power of `n` raised to the current iteration number `i` using the `math.Pow` function. It then checks if the calculated power is equal to `x`. If it is, the function returns `true`.

If the loop finishes without finding a match, the function returns `false`, indicating that `x` is not a simple power of `n`.

Note that the `math.Pow` function returns a floating-point number, so we need to convert `x` and `n` to floating-point numbers using the `float64` function. This is because the `math.Pow` function expects its arguments to be floating-point numbers.