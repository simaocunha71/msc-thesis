The problem is asking to write a function that takes the lengths of the three sides of a triangle as input and returns true if the three sides form a right-angled triangle, and false otherwise.

A right-angled triangle is a triangle in which one angle is 90 degrees. In a triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. This is known as the Pythagorean theorem.

Here's a Go solution for the problem:

```go
func RightAngleTriangle(a, b, c int) bool {
    if a > b && a > c {
        return b*b+c*c == a*a
    } else if b > a && b > c {
        return a*a+c*c == b*b
    } else if c > a && c > b {
        return a*a+b*b == c*c
    } else {
        return false
    }
}
```

This function first checks which side is the longest. If the longest side is a, it checks if the sum of the squares of the other two sides is equal to the square of the longest side. If it is, then the three sides form a right-angled triangle. If not, it checks the same condition for the other two sides. If none of the conditions are met, then the three sides do not form a right-angled triangle.