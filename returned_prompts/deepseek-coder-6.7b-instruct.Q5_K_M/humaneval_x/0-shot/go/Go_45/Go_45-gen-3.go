
return (a * h) / 2

}

*/

package main

import (
	"fmt"
)

func TriangleArea(a float64, h float64) float64 {
	return (a * h) / 2
}

func main() {
	fmt.Println(TriangleArea(5, 3))
}

// Output: 7.5
// This function works by calculating the area of a triangle using the formula: (base * height) / 2.
// Therefore, when the base is 5 and the height is 3, it returns 7.5.
