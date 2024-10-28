
    sort.Float64s(numbers)
    minDiff := math.MaxFloat64
    result := [2]float64{}

    for i := 0; i < len(numbers) - 1; i++ {
        if diff := numbers[i+1] - numbers[i]; diff < minDiff {
            minDiff = diff
            result[0] = numbers[i]
            result[1] = numbers[i+1]
        }
    }

    return result
}

```

## Solution

```go
package main

import (
	"fmt"
	"sort"
	"math"
)

func FindClosestElements(numbers []float64) [2]float64 {

	sort.Float64s(numbers)
	minDiff := math.MaxFloat64
	result := [2]float64{}

	for i := 0; i < len(numbers) - 1; i++ {
		if diff := numbers[i+1] - numbers[i]; diff < minDiff {
			minDiff = diff
			result[0] = numbers[i]
			result[1] = numbers[i+1]
		}
	}

	return result
}

func main() {
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2})) // [2.0 2.2]
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.0})) // [2.0 2.0]
}
```

## Explanation

This code defines a function `FindClosestElements` that takes as input a slice of floating point numbers, sorts it in ascending order, then iterates over the slice to find the two numbers that are closest to each other. The closest pair of numbers are then returned.

The `minDiff` variable is initialized to the maximum float value and is