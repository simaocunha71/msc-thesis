
return 0.5 * a * h
}

*/

package main

import "fmt"

func TriangleArea(a float64, h float64) float64 {
	return 0.5 * a * h
}

func main() {
	fmt.Println(TriangleArea(5, 3))
}

// 7.5

// The function TriangleArea calculates the area of a triangle by taking its base and height as parameters and returns the product of 0.5 and the base multiplied by the height.

// The main function calls the TriangleArea function with arguments 5 and 3 and prints its return value.

// The output of the program is 7.5, which is the area of a triangle with base 5 and height 3.

// This is a simple example of a function in Go that takes parameters and returns a value. The function is named TriangleArea and it calculates the area of a triangle given its base and height.

// The function is called with the arguments 5 and 3, and its return value is printed to the console.

// The output of the program is 7.5, which is the area of a triangle with base 5 and height 3.
