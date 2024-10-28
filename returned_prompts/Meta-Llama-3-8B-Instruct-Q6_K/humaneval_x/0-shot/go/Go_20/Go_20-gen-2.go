```go
package main

import (
	"fmt"
	"math"
)

func FindClosestElements(numbers []float64) [2]float64 {
	if len(numbers) < 2 {
		return [2]float64{}
	}
	minDiff := math.MaxFloat64
	closestElements := [2]float64{}

	for i := 0; i < len(numbers); i++ {
		for j := i + 1; j < len(numbers); j++ {
			diff := math.Abs(numbers[j] - numbers[i])
			if diff < minDiff {
				minDiff = diff
				closestElements[0] = numbers[i]
				closestElements[1] = numbers[j]
			}
		}
	}

	return closestElements
}

func main() {
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2}))
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.0}))
}
```


Explanation:
The function `FindClosestElements` takes a slice of float64 numbers as input and returns a slice of two numbers that are closest to each other.

First, it checks if the input slice has less than 2 elements. If so, it returns an empty slice.

Then, it initializes two variables: `minDiff` to store the minimum difference between two numbers, and `closestElements` to store the two numbers with the minimum difference.

The function then iterates over the input slice using two nested loops. The outer loop iterates over each element in the slice, and the inner loop iterates over the elements that come after the current element in the outer loop.

For each pair of numbers, it calculates the absolute difference between them and checks if it's less than the current minimum difference. If it is, it updates `minDiff` and `closestElements`.

Finally, the function returns `closestElements`.

In the `main` function, we test the `FindClosestElements` function with two examples. The first example returns `(2.0, 2.2)` because 2.0 and 2.2 are the closest numbers in the slice. The second example returns `(2.0, 2.0)` because 2.0 is the only number that appears twice in