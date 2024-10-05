```go
func RightAngleTriangle(a, b, c int) bool {
    if a*a+b*b == c*c || a*a+c*c == b*b || b*b+c*c == a*a {
        return true
    }
    return false
}
```
The idea is to use the Pythagorean theorem, which states that for a right-angled triangle, the square of the hypotenuse side is equal to the sum of squares of the other two sides. We check if any two sides form a right-angled triangle by checking if the square of the third side is equal to the sum of squares of the other two sides. If it is, we return true; otherwise, we return false. This function takes three integer arguments, a, b, and c, which represent the lengths of the sides of the triangle. It returns a boolean value indicating whether the sides form a right-angled triangle. The function uses the Pythagorean theorem to check if the sides form a right-angled triangle. If the square of the hypotenuse side is equal to the sum of squares of the other two sides, it returns true; otherwise, it returns false. This function is efficient and accurate in determining whether the given sides form a right-angled triangle.