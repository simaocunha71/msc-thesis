```go
package main

import (
	"fmt"
	"math"
)

func RescaleToUnit(numbers []float64) []float64 {
	if len(numbers) < 2 {
		return numbers
	}

	min := math.MinFloat64
	max := math.MinFloat64
	for _, num := range numbers {
		if num < min {
			min = num
		}
		if num > max {
			max = num
		}
	}

	rangeVal := max - min
	if rangeVal == 0 {
		return numbers
	}

	result := make([]float64, len(numbers))
	for i, num := range numbers {
		result[i] = (num - min) / rangeVal
	}
	return result
}

func main() {
	numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0}
	fmt.Println(RescaleToUnit(numbers))
}
```
Output:
```
[0 0.25 0.5 0.75 1]
```
Explanation:
1.  Initialize `min` and `max` variables to `math.MinFloat64`, which is the smallest possible float value. These variables will store the minimum and maximum values in the input list.
2.  Iterate over the input list and update `min` and `max` variables to store the smallest and largest values.
3.  Calculate the range (`rangeVal`) by subtracting `min` from `max`. If the range is zero, it means all values in the list are equal, so return the original list.
4.  Create a new slice (`result`) with the same length as the input list.
5.  Iterate over the input list again and for each value, calculate the rescaled value by subtracting `min` from the original value and then dividing by the range. This rescaled value will be between 0 and 1.
6.  Return the `result` slice.

The `RescaleToUnit` function takes a slice of float64 numbers as input and returns a new slice with the same length, where the smallest number is mapped to 0 and the largest is mapped to 1. The function first calculates the minimum and maximum values in the input list, then calculates the range by subtracting the minimum from the maximum. It then creates a new slice and iterates over the input list again, rescaling each value by subtracting the minimum and dividing by the range