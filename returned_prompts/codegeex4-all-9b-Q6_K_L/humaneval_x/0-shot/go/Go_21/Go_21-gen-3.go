You can solve this problem by using the `math` package in Go. Here's how you can do it:

```go
package main

import (
	"fmt"
	"math"
)

func RescaleToUnit(numbers []float64) []float64 {
	min := math.Inf(1)
	max := math.Inf(-1)

	for _, num := range numbers {
		if num < min {
			min = num
		}
		if num > max {
			max = num
		}
	}

	for i := range numbers {
		numbers[i] = (numbers[i] - min) / (max - min)
	}

	return numbers
}

func main() {
	numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0}
	rescaled := RescaleToUnit(numbers)
	fmt.Println(rescaled)
}
```

In this code, we first find the minimum and maximum values in the `numbers` slice. Then, we use these values to transform the numbers in the slice so that the smallest number becomes 0 and the largest becomes 1. Finally, we print the transformed numbers.