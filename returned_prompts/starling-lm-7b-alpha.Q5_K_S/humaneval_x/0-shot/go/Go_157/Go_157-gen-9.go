To determine if a triangle with sides of length a, b, and c is a right angle triangle,
we can use the Pythagorean theorem, which states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.

In other words, we need to check whether the following equation holds true:

a^2 + b^2 == c^2

To solve this equation, we can follow these steps:

1. Square the length of side a, and store the result in variable aSquared.
2. Square the length of side b, and store the result in variable bSquared.
3. Square the length of side c, and store the result in variable cSquared.
4. Add the values of aSquared and bSquared, and store the result in variable sum.
5. Compare the value of sum to cSquared.
6. If sum equals cSquared, return true, indicating that the triangle is a right-angled triangle. Otherwise, return false.

Here's the code that implements these steps:

```go
func RightAngleTriangle(a, b, c int) bool {
    aSquared := a * a
    bSquared := b * b
    cSquared := c * c
    sum := aSquared + bSquared
    return sum == cSquared
}
```

This implementation uses the multiplication operator (*) to perform squaring, as it is more efficient than using the exponentiation operator (**) in Go.

You can use the RightAngleTriangle function as follows:

```go
fmt.Println(RightAngleTriangle(3, 4, 5))  // Output: true
fmt.Println(RightAngleTriangle(1, 2, 3))  // Output: false
```

These calls to RightAngleTriangle will return true and false, respectively, indicating whether the triangles with sides of length 3, 4, and 5, and 1, 2, and 3 are right-angled triangles or not.

```

```