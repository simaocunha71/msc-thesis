    sum := 0.0
    for _, num := range lst {
        if num > 0 && math.Mod(num, 1) == 0 && int(num) % 2 != 0 {
            sum += math.Pow(num, 2)
        }
    }
    return int(sum)
}

*/

// Package main provides ...
package main

import (
	"fmt"
)

// Given a list of numbers, return the sum of squares of the numbers
// in the list that are odd. Ignore numbers that are negative or not integers.
func DoubleTheDifference(lst []float64) int {
	sum := 0.0
	for _, num := range lst {
		if num > 0 && num == float64(int(num)) && int(num)%2 != 0 {
			sum += num * num
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

// This is a modification of the original code where we use num == float64(int(num)) instead of math.Mod(num, 1) == 0 to check if the number is an integer.
// This is because the only way to check if a float is an integer in Go is to compare it to its integer equivalent by using num == float64(int(num)).
// This way we avoid using the math package.

/*
Here's a brief explanation of the modified code:

1. We define a function DoubleTheDifference that takes a slice of float64 as input.
2. Inside the function, we initialize a variable sum to 0.0.
3. We then iterate over the input slice. For each number in the slice, we check