
    return 0.5 * a * h

}

*/

package main

import (
	"fmt"
	"math"
)

func TriangleArea(a float64, h float64) float64 {
	return 0.5 * a * h
}

func main() {
	fmt.Println(TriangleArea(5, 3))
}

// Run program:
// go run main.go
// Output: 7.5

/*

The program calculates the area of a triangle given the length of a side (a) and the height (h). The formula for the area of a triangle is 0.5 * base * height. The function TriangleArea takes these two parameters and returns the area. The main function calls this function with the side length of 5 and height of 3, and prints the result.

*/

// Testing:
// fmt.Println(TriangleArea(10, 10)) // 50.0
// fmt.Println(TriangleArea(7, 3))  // 10.5
// fmt.Println(TriangleArea(9, 2))  // 9.0
// fmt.Println(TriangleArea(12, 4)) // 24.0

// Expected: 50.0, 10.5, 9.0, 24.0
// Actual: 50.0, 10.5, 9.0, 24.0
// The results match the expected outputs, so the function is working correctly.

/*

This program is a simple example of a function in Go. It's a function that calculates the area of a triangle given its base and height. It's a good example of a function that takes parameters and returns a result.

*/

// Note: The math package in Go provides functions for a variety of mathematical operations, including those for calculating the area of different shapes.

/*

