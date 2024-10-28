Here is the solution to the problem:

```go
import (
    "math"
)

// Given the lengths of the three sides of a triangle. Return the area of
// the triangle rounded to 2 decimal points if the three sides form a valid triangle.
// Otherwise return -1
// Three sides make a valid triangle when the sum of any two sides is greater
// than the third side.
// Example:
// TriangleArea(3, 4, 5) == 6.00
// TriangleArea(1, 2, 10) == -1
func TriangleArea(a float64, b float64, c float64) interface{} {
    // Check if the three sides form a valid triangle
    if a+b <= c || a+c <= b || b+c <= a {
        return -1
    }

    // Calculate the semi-perimeter of the triangle
    s := (a + b + c) / 2

    // Calculate the area of the triangle using Heron's formula
    area := math.Sqrt(s*(s-a)*(s-b)*(s-c))

    // Round the area to 2 decimal points
    return math.Round(100*area) / 100
}
```

This function first checks if the three sides form a valid triangle by verifying the triangle inequality theorem. If the three sides do not form a valid triangle, the function returns -1. If the three sides do form a valid triangle, the function calculates the semi-perimeter of the triangle and then uses Heron's formula to calculate the area of the triangle. Finally, the function rounds the area to 2 decimal points and returns it.