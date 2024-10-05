```go
package main

import (
	"fmt"
	"math"
)

func FindClosestElements(numbers []float64) [2]float64 {
	minDiff := math.MaxFloat64
	var closest [2]float64
	for i := 0; i < len(numbers); i++ {
		for j := i + 1; j < len(numbers); j++ {
			diff := math.Abs(numbers[j] - numbers[i])
			if diff < minDiff {
				minDiff = diff
				closest[0] = numbers[i]
				closest[1] = numbers[j]
			}
		}
	}
	return closest
}

func main() {
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2}))
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.0}))
}
```
The program defines a function `FindClosestElements` that takes a slice of `float64` numbers and returns a slice of two `float64` numbers that are closest to each other. The function iterates over the input slice and for each number, it calculates the difference with all other numbers in the slice. It keeps track of the smallest difference and the corresponding numbers. The function returns these numbers in the order of their appearance in the input slice. If the input slice contains duplicate numbers, the function will return the first pair of identical numbers it finds.

In the `main` function, the program tests the `FindClosestElements` function with two examples. The first example returns `(2.0, 2.2)` and the second example returns `(2.0, 2.0)`. The program uses `fmt.Println` to print the results.