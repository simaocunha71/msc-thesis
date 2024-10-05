```go
func Simplify(x, n string) bool {
    a, err := strconv.ParseFloat(x, 64)
    if err != nil {
        panic(err)
    }
    b, err := strconv.ParseFloat(n, 64)
    if err != nil {
        panic(err)
    }
    result := a * b
    return result == float64(int(result))
}
```
The function `Simplify` takes two string parameters `x` and `n` representing fractions in the format `<numerator>/<denominator>`. It parses the strings to `float64` and multiplies them. Then it checks if the result is equal to the integer part of the result. If they are equal, the function returns `true`; otherwise, it returns `false`. 

The `strconv.ParseFloat` function is used to convert the string to a `float64`. The second argument `64` specifies the precision of the conversion. The `panic` function is used to stop the program if the conversion fails, as the problem statement assumes that the input strings are valid fractions. 

The `int(result)` function is used to get the integer part of the result, and `float64(int(result))` is used to convert the integer back to a `float64` for comparison with `result`. 

Note that this function does not simplify the fractions, it just checks if the result of multiplying them is a whole number. If you want to simplify the fractions, you would need a more complex function that finds the greatest common divisor of the numerator and denominator, and then divides both by the GCD. 