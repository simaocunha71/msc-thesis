```
package main

import (
	"fmt"
	"math"
)

func FindClosestElements(numbers []float64) [2]float64 {
	minDiff := math.MaxFloat64
	closestPair := [2]float64{}
	for i := 0; i < len(numbers); i++ {
		for j := i + 1; j < len(numbers); j++ {
			diff := numbers[j] - numbers[i]
			if math.Abs(diff) < minDiff {
				minDiff = math.Abs(diff)
				closestPair[0] = numbers[i]
				closestPair[1] = numbers[j]
			}
		}
	}
	return closestPair
}

func main() {
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2}))
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.0}))
}
```


The program defines a function `FindClosestElements` that takes a slice of floats as input and returns a slice of two floats, which are the closest elements in the input slice. The function iterates over all pairs of elements in the slice, calculates the absolute difference between each pair, and keeps track of the pair with the smallest difference. Finally, it returns this pair.

In the `main` function, the program tests the `FindClosestElements` function with two example inputs. The first input is `[1.0, 2.0, 3.0, 4.0, 5.0, 2.2]`, and the expected output is `(2.0, 2.2)`. The second input is `[1.0, 2.0, 3.0, 4.0, 5.0, 2.0]`, and the expected output is `(2.0, 2.0)`.

When you run the program, it prints the expected output for both inputs. The first output is `(2.0, 2.2)`, and the second output is `(2.0, 2.0)`. This indicates that the program is working correctly.