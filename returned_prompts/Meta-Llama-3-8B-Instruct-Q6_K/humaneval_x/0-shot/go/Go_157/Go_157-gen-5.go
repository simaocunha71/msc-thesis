```go
func RightAngleTriangle(a, b, c int) bool {
    if a*a+b*b == c*c || a*a+c*c == b*b || b*b+c*c == a*a {
        return true
    }
    return false
}
```


Explanation:
The function checks if the sum of the squares of two sides of the triangle is equal to the square of the third side. This is a necessary and sufficient condition for the triangle to be right-angled. The function uses the Pythagorean theorem, which states that in a right-angled triangle, the square of the hypotenuse side is equal to the sum of squares of the other two sides. The function checks all three possible combinations of sides and returns true if any of them satisfy the condition, and false otherwise.