```go
func Iscube(a int) bool {
    c := int(math.Ceil(math.Pow(float64(a), (1.0/3.0))))
    return c * c * c == int64(a)
}
```
Explanation:

The problem is asking to write a function that takes an integer `a` as input and returns `true` if this integer is a cube of some integer number. The function should return `false` otherwise.

We can solve this problem by taking the cube root of the input integer `a` and then checking if the result is an integer. If it is, then `a` is a cube of some integer number.

In the code, we use the `math.Pow` function to calculate the cube root of `a` and then use the `math.Ceil` function to round up the result to the nearest integer. We then check if the cube of this integer is equal to `a`. If it is, we return `true`; otherwise, we return `false`.

Note that we use `int64(a)` to convert the result of `a` to an `int64` before comparing it with the cube of the integer, because the result of `a` might be too large to fit in an `int` variable. We also use `c * c * c` to calculate the cube of the integer `c`, because the `*` operator has higher precedence than the `==` operator in Go.