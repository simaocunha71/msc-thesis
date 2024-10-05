```go
package main

import (
	"fmt"
	"math"
)

func FindClosestElements(numbers []float64) [2]float64 {
	minDiff := math.MaxFloat64
	var closestNumbers [2]float64

	for i := 0; i < len(numbers); i++ {
		for j := i + 1; j < len(numbers); j++ {
			diff := math.Abs(numbers[j] - numbers[i])
			if diff < minDiff {
				minDiff = diff
				closestNumbers[0] = numbers[i]
				closestNumbers[1] = numbers[j]
			}
		}
	}

	return closestNumbers
}

func main() {
	numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2}
	closest := FindClosestElements(numbers)
	fmt.Println(closest)
}
```


This program uses two nested loops to compare each pair of numbers in the input list. For each pair, it calculates the absolute difference between the two numbers. If the difference is less than the current minimum difference, it updates the minimum difference and the closest numbers. Finally, it returns the closest numbers in the order they appear in the list. In the main function, we test the FindClosestElements function with the example input. The output will be `(2.0, 2.2)`. If there are multiple pairs of numbers with the same minimum difference, this program will return the first pair it finds. If you want to return all pairs with the same minimum difference, you would need to modify the program to keep track of all such pairs.