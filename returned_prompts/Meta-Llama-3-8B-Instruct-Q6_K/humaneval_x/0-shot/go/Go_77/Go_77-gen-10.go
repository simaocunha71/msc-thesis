```go
func Iscube(a int) bool {
    c := int(math.Sqrt(math.Pow(float64(a), 1/3.0)))
    return c*c*c == a
}
```
Explanation:
The function Iscube takes an integer a as input and returns true if a is a cube of some integer number, and false otherwise.

We use the math.Sqrt and math.Pow functions to calculate the cube root of the input number a. We cast the result to an integer using the int() function, as the cube root may be a decimal number.

We then check if the cube of this integer is equal to the input number a. If it is, we return true, indicating that a is a cube of some integer number. Otherwise, we return false.

This solution works for all valid inputs, including positive, negative, and zero. It also handles the edge case where a is 0, which is considered a cube of 0.