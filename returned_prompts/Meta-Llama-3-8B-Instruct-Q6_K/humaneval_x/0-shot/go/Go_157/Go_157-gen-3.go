The problem is asking to write a function that takes the lengths of three sides of a triangle as input and returns true if the triangle is a right-angled triangle, and false otherwise.

A right-angled triangle is a triangle in which one angle is a right angle or 90 degrees. This means that the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.

Here is the solution in Go:
```go
func RightAngleTriangle(a, b, c int) bool {
    // Calculate the square of the length of the hypotenuse
    hypotenuseSquared := a*a + b*b
    // Check if the square of the length of the hypotenuse is equal to the square of the length of the third side
    return c*c == hypotenuseSquared
}
```
This function calculates the square of the length of the hypotenuse using the formula `a*a + b*b`, and then checks if this value is equal to the square of the length of the third side `c*c`. If it is, the function returns true, indicating that the three sides form a right-angled triangle. Otherwise, it returns false.