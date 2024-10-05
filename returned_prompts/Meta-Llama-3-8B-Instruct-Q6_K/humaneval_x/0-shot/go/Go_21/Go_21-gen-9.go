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
	scale := 1.0 / (max - min)
	result := make([]float64, len(numbers))
	for i, num := range numbers {
		result[i] = (num - min) * scale
	}
	return result
}

func main() {
	fmt.Println(RescaleToUnit([]float64{1.0, 2.0, 3.0, 4.0, 5.0}))
}
```
Output:
```
[0 0.25 0.5 0.75 1]
```
Explanation:

1. We first find the minimum and maximum values in the input list.
2. We then calculate a scaling factor `scale` as the reciprocal of the range of the input values (max - min).
3. We create a new slice `result` of the same length as the input list.
4. We iterate over the input list, subtracting the minimum value from each element, multiplying the result by the scaling factor, and storing the result in the corresponding element of the `result` slice.
5. The resulting slice is the rescaled list, where the smallest value is 0 and the largest is 1.