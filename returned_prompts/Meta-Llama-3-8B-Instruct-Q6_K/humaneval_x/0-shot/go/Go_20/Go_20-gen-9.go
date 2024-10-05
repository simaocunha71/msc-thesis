```go
package main

import (
	"fmt"
	"math"
)

func FindClosestElements(numbers []float64) [2]float64 {
	minDiff := math.MaxFloat64
	var closestElements [2]float64

	for i := 0; i < len(numbers); i++ {
		for j := i + 1; j < len(numbers); j++ {
			diff := math.Abs(numbers[i] - numbers[j])
			if diff < minDiff {
				minDiff = diff
				closestElements[0] = numbers[i]
				closestElements[1] = numbers[j]
			}
		}
	}

	return closestElements
}

func main() {
	numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2}
	closestElements := FindClosestElements(numbers)
	fmt.Println(closestElements)
}
```
The function `FindClosestElements` takes a slice of floats as an argument and returns a slice of two floats that are the closest to each other. It iterates over all pairs of elements in the slice and calculates the absolute difference between each pair. It keeps track of the pair with the smallest difference and returns this pair.

The time complexity of this function is O(n^2), where n is the length of the input slice, because it iterates over all pairs of elements. The space complexity is O(1), because it only uses a constant amount of space to store the minimum difference and the closest elements.

In the `main` function, we create a slice of floats and call `FindClosestElements` with this slice as an argument. We then print the result to the console. When we run this program, it will output `(2.0, 2.2)` or `(2.0, 2.0)` depending on the input slice.