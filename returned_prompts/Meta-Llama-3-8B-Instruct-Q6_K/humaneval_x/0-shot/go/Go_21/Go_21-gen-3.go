```go
package main

import (
	"fmt"
	"math"
)

func RescaleToUnit(numbers []float64) []float64 {
	if len(numbers) < 2 {
		return nil
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

In this Go program, we first find the minimum and maximum values in the input slice of numbers. Then we calculate a scale factor to map the minimum to 0 and the maximum to 1. Finally, we create a new slice where each element is the corresponding element from the input slice scaled according to the calculated scale factor. The `RescaleToUnit` function returns this new slice.

The `main` function demonstrates the usage of the `RescaleToUnit` function by printing the result of rescaling the slice `[1.0, 2.0, 3.0, 4.0, 5.0]`. The output will be `[0.0, 0.25, 0.5, 0.75, 1.0]`.