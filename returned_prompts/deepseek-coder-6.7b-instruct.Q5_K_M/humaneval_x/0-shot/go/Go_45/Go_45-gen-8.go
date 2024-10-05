
	return 0.5 * a * h
}

func main() {
	fmt.Println(TriangleArea(5, 3))
}

*/

package main

import "fmt"

// Given length of a side and high return area for a triangle.
func TriangleArea(a float64, h float64) float64 {
	return 0.5 * a * h
}

func main() {
	fmt.Println(TriangleArea(5, 3))
}
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("%.2f", SquaredError(10, 2))
}

// Calculate squared error between two numbers.
func SquaredError(a float64, b float64) float64 {
	return math.Pow((a - b), 2)
}

// 