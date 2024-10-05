You can use the sort package to sort the numbers and then apply the linear transformation based on the sorted numbers. Here's an example implementation:

```go
package main

import (
	"fmt"
	"sort"
)

func RescaleToUnit(numbers []float64) []float64 {
	sort.Float64s(numbers)
	min := numbers[0]
	max := numbers[len(numbers)-1]
	for i := range numbers {
		numbers[i] = (numbers[i] - min) / (max - min)
	}
	return numbers
}

func main() {
	numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0}
	rescaled := RescaleToUnit(numbers)
	fmt.Println(rescaled) // Output: [0 0.25 0.5 0.75 1]
}
```

In this implementation, we first sort the numbers using `sort.Float64s(numbers)`. Then, we calculate the minimum and maximum values from the sorted numbers. Finally, we apply the linear transformation to each number in the original list by subtracting the minimum value and dividing by the range (max - min).

Note that this implementation modifies the input slice directly. If you want to keep the original slice unchanged, you can create a copy of the slice before applying the transformation.