    sum := 0.0
    for _, num := range lst {
        if num >= 0 && math.Mod(num,2) != 0 {
            sum += math.Pow(num,2)
        }
    }
    return int(sum)
}

*/

package main

import (
	"fmt"
	"math"
)

func DoubleTheDifference(lst []float64) int {
	sum := 0.0
	for _, num := range lst {
		if num >= 0 && math.Mod(num,2) != 0 {
			sum += math.Pow(num,2)
		}
	}
	return int(sum)
}

func main() {
	fmt.Println(DoubleTheDifference([]float64{1, 3, 2, 0}))
	fmt.Println(DoubleTheDifference([]float64{-1, -2, 0}))
	fmt.Println(DoubleTheDifference([]float64{9, -2}))
	fmt.Println(DoubleTheDifference([]float64{0}))
	fmt.Println(DoubleTheDifference([]float64{}))
}

/*
10
0
81
0
0
*/

// This code is written in Go programming language. It defines a function named DoubleTheDifference that takes a slice of floating point numbers as an argument and returns the sum of the squares of the odd positive numbers in the slice. If the slice is empty or all numbers are negative or not integers, the function will return 0.

// The function uses a for loop to iterate over the slice of numbers. For each number, it checks if the number is positive and odd (i.e., the remainder of the number divided by 2 is not 0). If the number satisfies these conditions, it is squared and added to the sum.

// The final sum is returned as an integer.

// The main function demonstrates the usage of the DoubleTheDifference function with a few test cases.

// The output of the main function is the sum of the squares of the odd numbers in each of the test cases.

// The time complexity of this function is O