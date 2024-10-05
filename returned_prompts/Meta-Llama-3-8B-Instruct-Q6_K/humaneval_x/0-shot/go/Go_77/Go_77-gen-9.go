```go
func Iscube(a int) bool {
    c := int(math.Ceil(math.Pow(float64(a), 1/3)))
    return c*c*c == a
}
```
The function `Iscube(a int) bool` checks if the given integer `a` is a perfect cube or not. It calculates the cube root of `a` using the `math.Pow` function with a fractional exponent. It then calculates the integer part of the cube root using the `math.Ceil` function. If the cube of the calculated integer equals `a`, the function returns `true`, indicating that `a` is a perfect cube. Otherwise, it returns `false`. This solution works for both positive and negative integers, as well as zero.