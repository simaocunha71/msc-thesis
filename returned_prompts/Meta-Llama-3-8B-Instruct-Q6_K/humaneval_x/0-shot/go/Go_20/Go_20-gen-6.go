```
package main

import (
	"fmt"
	"math"
)

func FindClosestElements(numbers []float64) [2]float64 {
	minDiff := math.MaxFloat64
	closestPair := [2]float64{}
	for i := 0; i < len(numbers); i++ {
		for j := i + 1; j < len(numbers); j++ {
			diff := math.Abs(numbers[j] - numbers[i])
			if diff < minDiff {
				minDiff = diff
				closestPair[0] = numbers[i]
				closestPair[1] = numbers[j]
			}
		}
	}
	return closestPair
}

func main() {
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2})) // (2.0, 2.2)
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.0})) // (2.0, 2.0)
}
```

This code defines a function `FindClosestElements` that takes a slice of floating-point numbers as input and returns a pair of numbers that are the closest to each other. The function iterates over the input slice, comparing each pair of numbers to find the pair with the smallest difference.

The `main` function tests the `FindClosestElements` function with two different input slices and prints the results.

Note that this code uses the `math.Abs` function to calculate the absolute difference between two numbers, and the `math.MaxFloat64` constant to initialize the minimum difference to a large value. The `closestPair` variable is used to store the pair of numbers with the smallest difference, and is returned at the end of the function.