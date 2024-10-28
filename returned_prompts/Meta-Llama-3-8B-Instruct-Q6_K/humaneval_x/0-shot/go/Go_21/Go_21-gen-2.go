```go
package main

import (
	"fmt"
	"math"
)

func RescaleToUnit(numbers []float64) []float64 {
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
	if max-min == 0 {
		return numbers // all numbers are equal, return original list
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
