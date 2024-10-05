```go
package main

import (
	"fmt"
)

func TriangleArea(a float64, b float64, c float64) interface{} {
	if a+b <= c || a+c <= b || b+c <= a {
		return -1
	}

	// Calculate the semi-perimeter
	s := (a + b + c) / 2

	// Calculate the area using Heron's formula
	area := math.Sqrt(s * (s - a) * (s - b) * (s - c))

	// Round to 2 decimal points
	area = math.Round(area*100) / 100

	return area
}

func main() {
	fmt.Println(TriangleArea(3, 4, 5))  // Output: 6.00
	fmt.Println(TriangleArea(1, 2, 10)) // Output: -1
}
```
