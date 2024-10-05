To achieve the desired transformation where the smallest number in the list becomes 0 and the largest becomes 1, you can follow these steps:

1. Find the minimum and maximum values in the list.
2. Subtract the minimum value from all numbers in the list to make the minimum 0.
3. Divide all numbers by the range (maximum - minimum) to make the maximum 1.

Here's how you can implement this in Go:

```go
package main

import (
	"fmt"
)

// RescaleToUnit rescales a slice of float64 numbers so that the smallest number becomes 0 and the largest becomes 1
func RescaleToUnit(numbers []float64) []float64 {
	// Find the minimum and maximum values
	min := numbers[0]
	max := numbers[0]
	for _, num := range numbers {
		if num < min {
			min = num
		}
		if num > max {
			max = num
		}
	}

	// Rescale the numbers
	rescaled := make([]float64, len(numbers))
	for i, num := range numbers {
		rescaled[i] = (num - min) / (max - min)
	}

	return rescaled
}

func main() {
	numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0}
	rescaled := RescaleToUnit(numbers)
	fmt.Println(rescaled) // Output: [0 0.25 0.5 0.75 1]
}
```

In this code, the `RescaleToUnit` function takes a slice of `float64` numbers as input and returns a new slice with the rescaled values. The function first finds the minimum and maximum values in the input slice, then rescales each number based on these values. The result is a slice where the smallest number is 0 and the largest is 1, as desired.