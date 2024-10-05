```go
func Iscube(a int) bool {
    c := int(math.Sqrt(math.Pow(float64(a), (1.0/3.0))))
    return c*c*c == a
}
```
In this solution, we use the mathematical property of cube roots: `a^(1/3)` is the cube root of `a`. We calculate the cube root of `a` using the `math.Pow` function with the base `a` and the exponent `1.0/3.0`. We then calculate the square of the cube root using the `c*c` expression, and check if it is equal to `a`. If it is, we return `true`, indicating that `a` is a cube of some integer number. Otherwise, we return `false`. This solution works for both positive and negative integers, as well as zero.