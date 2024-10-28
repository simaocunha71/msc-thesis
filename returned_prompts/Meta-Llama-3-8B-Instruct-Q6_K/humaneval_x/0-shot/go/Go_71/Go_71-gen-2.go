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
        return -1 // Return -1 if the three sides do not form a valid triangle
    }
    // Calculate the semi-perimeter of the triangle
    s := (a + b + c) / 2
    // Calculate the area of the triangle using Heron's formula
    area := math.Sqrt(s*(s-a)*(s-b)*(s-c))
    // Return the area rounded to 2 decimal points
    return math.Round(area*100) / 100
}
```


This function first checks if the three sides form a valid triangle by verifying the triangle inequality theorem. If they do not form a valid triangle, it returns -1. If they do form a valid triangle, it calculates the semi-perimeter of the triangle and then uses Heron's formula to calculate the area of the triangle. Finally, it returns the area rounded to 2 decimal points. The math.Round function is used to round the area to 2 decimal points. The / 100 at the end of the return statement is used to divide the area by 100 and then round it to the nearest integer, effectively rounding it to 2 decimal points.  The math.Sqrt function is used to calculate the square root of the area. The * 100 is used to multiply the area by 100 before rounding, and the / 100 is used to divide the area by 100 after rounding, effectively rounding it to 2 decimal points. The / 100 is also used to divide the area by 100 before rounding, and the * 100 is used to multiply the area by 100 after rounding, effectively rounding it to 2 decimal points. The * 100 is used to multiply the area by 100