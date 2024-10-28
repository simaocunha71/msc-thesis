Here is the solution to the problem:

```go
import (
    "math"
    "fmt"
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
    // Calculate the area
    area := math.Sqrt(s*(s-a)*(s-b)*(s-c))
    // Round the area to 2 decimal points
    return fmt.Sprintf("%.2f", area)
}

```


This function first checks if the three sides form a valid triangle by ensuring that the sum of any two sides is greater than the third side. If they do not form a valid triangle, it returns -1.

If the sides do form a valid triangle, it calculates the semi-perimeter and then uses Heron's formula to calculate the area of the triangle. The area is then rounded to 2 decimal points and returned. The area is returned as a string, which is why the function returns an interface{}. This is because Go does not have a built-in way to return multiple values with different types. The area is returned as a string, and the function returns an interface{} to represent this. The caller of the function can then use the `fmt.Sprintf` function to convert the string back to a float64 if needed.