Here is a Go function that solves the problem. This function uses the Heron's formula to calculate the area of the triangle. It first checks if the three sides form a valid triangle by verifying the triangle inequality theorem. If the sides do not form a valid triangle, it returns -1. Otherwise, it calculates the semi-perimeter of the triangle and then uses Heron's formula to calculate the area.

```go
package main

import (
    "math"
)

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

func main() {
    result := TriangleArea(3, 4, 5)
    if result != 6.0 {
        panic("Expected 6.0, got " + string(result))
    }

    result = TriangleArea(1, 2, 10)
    if result != -1 {
        panic("Expected -1, got " + string(result))
    }
}
```

This function will return the area of the triangle as a float64 value, rounded to 2 decimal points. If the three sides do not form a valid triangle, it will return -1. The main function demonstrates how to use this function with the examples provided in the problem description. It checks if the returned value is correct and panics if it is not. This is a simple test to ensure that the function is working as expected.