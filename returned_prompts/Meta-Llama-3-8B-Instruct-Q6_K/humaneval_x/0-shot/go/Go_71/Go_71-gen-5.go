Here is a Go program that calculates the area of a triangle given the lengths of its three sides. It uses Heron's formula to calculate the area of the triangle.

```go
package main

import (
    "math"
    "fmt"
)

// Given the lengths of the three sides of a triangle. Return the area of
// the triangle rounded to 2 decimal points if the three sides form a valid triangle.
// Otherwise return -1
// Three sides make a valid triangle when the sum of any two sides is greater
// than the third side.
func TriangleArea(a float64, b float64, c float64) interface{} {
    // Check if the three sides form a valid triangle
    if a+b <= c || a+c <= b || b+c <= a {
        return -1
    }

    // Calculate the semi-perimeter
    s := (a + b + c) / 2

    // Calculate the area using Heron's formula
    area := math.Sqrt(s*(s-a)*(s-b)*(s-c))

    // Return the area rounded to 2 decimal points
    return fmt.Sprintf("%.2f", area)
}

func main() {
    fmt.Println(TriangleArea(3, 4, 5))  // Output: 6.00
    fmt.Println(TriangleArea(1, 2, 10)) // Output: -1
}
```

In this program, we first check if the three sides form a valid triangle by verifying that the sum of any two sides is greater than the third side. If they don't form a valid triangle, we return -1. If they do form a valid triangle, we calculate the semi-perimeter `s` and then use Heron's formula to calculate the area. We then return the area rounded to 2 decimal points using the `fmt.Sprintf` function. The `main` function tests the `TriangleArea` function with two examples. The first example should return 6.00, and the second example should return -1.