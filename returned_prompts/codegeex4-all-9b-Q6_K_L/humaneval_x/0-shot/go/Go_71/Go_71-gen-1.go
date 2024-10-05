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
    // Check if the sides form a valid triangle
    if a + b <= c || a + c <= b || b + c <= a {
        return -1
    }

    // Calculate the semi-perimeter
    s := (a + b + c) / 2

    // Calculate the area using Heron's formula
    area := math.Sqrt(s * (s - a) * (s - b) * (s - c))

    // Round the area to 2 decimal points
    area = math.Round(area * 100) / 100

    return area
}
```

This solution checks if the given sides can form a valid triangle by comparing the sum of any two sides with the third side. If the sides do not form a valid triangle, it returns -1. Otherwise, it calculates the semi-perimeter using the formula `(a + b + c) / 2` and then uses Heron's formula to calculate the area of the triangle. Finally, it rounds the area to 2 decimal points using the `math.Round` function and returns the result.