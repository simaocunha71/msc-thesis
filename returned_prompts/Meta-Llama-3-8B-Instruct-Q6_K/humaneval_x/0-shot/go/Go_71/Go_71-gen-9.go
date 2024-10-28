Here is the solution:
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

    // Calculate the semi-perimeter
    s := (a + b + c) / 2

    // Calculate the area using Heron's formula
    area := math.Sqrt(s*(s-a)*(s-b)*(s-c))

    // Round the area to 2 decimal points
    return math.Round(area*100) / 100
}
```


Explanation:

1. We first check if the three sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If not, we return -1.
2. If the three sides form a valid triangle, we calculate the semi-perimeter `s` as half the perimeter of the triangle.
3. We then calculate the area of the triangle using Heron's formula, which is `sqrt(s*(s-a)*(s-b)*(s-c))`.
4. Finally, we round the area to 2 decimal points by multiplying it by 100 and then dividing it by 100. The `math.Round` function is used to round the area to the nearest integer, and then we divide it by 100 to get the area rounded to 2 decimal points.

This solution works correctly for all valid triangles and returns -1 for invalid triangles. The area is rounded to 2 decimal points as required.