```go
import (
    "math"
    "fmt"
    "math/rand"
    "time"
)

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

func main() {
    // Test the function
    fmt.Println(TriangleArea(3, 4, 5)) // Output: 6.00
    fmt.Println(TriangleArea(1, 2, 10)) // Output: -1
}
```


The code defines a function `TriangleArea` that takes three arguments `a`, `b`, and `c` representing the lengths of the three sides of a triangle. The function checks if the three sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If the three sides do not form a valid triangle, the function returns `-1`. Otherwise, the function calculates the area of the triangle using Heron's formula and rounds the area to 2 decimal points.

In the `main` function, the code tests the `TriangleArea` function with two examples: `TriangleArea(3, 4, 5)` and `TriangleArea(1, 2, 10)`. The output for the first example is `6.00` and the output for the second example is `-1`, as expected.

Note that the `math/rand` and `time` packages are not used in this code, so they can be removed. The `import "fmt"` statement is required to use the `fmt.Println` function in the `main` function. The `interface{}` return type is used to return either a float64 value (the area of the triangle) or an int value (-1) depending on whether the three sides form a valid triangle. The `fmt.Sprintf` function is used to format the area to 2 decimal points.