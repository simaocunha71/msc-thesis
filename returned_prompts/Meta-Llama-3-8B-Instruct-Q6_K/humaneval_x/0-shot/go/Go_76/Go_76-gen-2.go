```go
func IsSimplePower(x int, n int) bool {
    if x == 1 {
        return true
    }
    for i := 2; i <= int(math.Pow(float64(n), float64(1/math.Log(float64(x), float64(n))))); i++ {
        if math.Pow(float64(n), float64(i)) == float64(x) {
            return true
        }
    }
    return false
}
```


The function `IsSimplePower` checks if a number `x` is a simple power of `n`. 

The function first checks if `x` is equal to 1, in which case it returns `true` because any number is a power of 1.

Then it uses a for loop to check all possible powers of `n` that are less than or equal to `x`. The loop variable `i` ranges from 2 to the ceiling of `x` divided by `n` (since `x` is a power of `n` if `x = n^i` for some `i`). 

Inside the loop, it checks if `n` raised to the power of `i` is equal to `x`. If it is, the function returns `true`.

If the function has checked all possible powers of `n` and hasn't found a match, it returns `false`, indicating that `x` is not a simple power of `n`. 

The function uses the `math.Pow` function to calculate the power of `n` and the `math.Log` function to calculate the log of `x` base `n`. The `int` and `float64` conversions are used to ensure that the calculations are done correctly. 

This function is not very efficient for large numbers, as it needs to check all possible powers of `n` up to `x`. For a more efficient solution, you could use a binary search or a more advanced algorithm. 

However, for the purpose of this problem, this function should work fine. 

This function is also not very robust, as it does not handle errors that might occur when calculating the power or log of `x` base `n`. In a real-world application, you would want to add error checking code to handle these cases. 





Final Answer: The final answer is the given code. I hope it is correct.