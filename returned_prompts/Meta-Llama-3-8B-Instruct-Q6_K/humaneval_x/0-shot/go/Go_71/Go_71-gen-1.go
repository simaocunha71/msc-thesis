```go
package main

import (
    "math"
    "fmt"
)

func TriangleArea(a float64, b float64, c float64) interface{} {
    // Check if the sides form a valid triangle
    if a+b <= c || a+c <= b || b+c <= a {
        return -1.0
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
In this solution, we first check if the three sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If not, we return -1.0.

If the sides form a valid triangle, we calculate the semi-perimeter using the formula `s = (a + b + c) / 2`. Then, we calculate the area using Heron's formula `area = sqrt(s*(s-a)*(s-b)*(s-c))`.

Finally, we return the area rounded to 2 decimal points using the `fmt.Sprintf` function with the format string `%.2f`. This is because the `interface{}` return type allows us to return a string representation of the area. In the `main` function, we demonstrate the usage of the `TriangleArea` function with two examples. The first example returns the area of a valid triangle, while the second example returns -1.0 because the sides do not form a valid triangle.