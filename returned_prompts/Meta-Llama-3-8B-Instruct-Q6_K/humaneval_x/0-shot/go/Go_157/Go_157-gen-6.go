Here is a possible solution:
```go
func RightAngleTriangle(a, b, c int) bool {
    // Check if the sum of the squares of two sides is equal to the square of the third side
    // This is a necessary condition for a triangle to be right-angled
    if a*a+b*b == c*c || a*a+c*c == b*b || b*b+c*c == a*a {
        return true
    }
    return false
}
```
This function checks if the sum of the squares of two sides is equal to the square of the third side. If it is, then the three sides form a right-angled triangle. If not, then they do not. This is a necessary condition for a triangle to be right-angled, but it is not sufficient (i.e., there may be non-right-angled triangles that also satisfy this condition). However, in the context of this problem, we are only interested in determining whether the three sides form a right-angled triangle, and this condition is sufficient for that purpose.