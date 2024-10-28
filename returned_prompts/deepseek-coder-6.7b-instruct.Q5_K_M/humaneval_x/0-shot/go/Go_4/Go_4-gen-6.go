    if len(numbers) == 0 {
        return 0.0
    }
    sum := 0.0
    for _, num := range numbers {
        sum += math.Abs(num)
    }
    mean := sum / float64(len(numbers))

B:
    sum = 0.0
    for _, num := range numbers {
        sum += math.Abs(num - mean)
    }

C:
    mad := sum / float64(len(numbers))
    return mad
}

This function takes a slice of numbers as an input, calculates the mean, and then computes the mean absolute deviation from this mean.

The function first calculates the mean of the input data and then calculates the sum of the absolute differences between each number and the mean. This sum is divided by the number of elements in the dataset to get the mean absolute deviation.

If the dataset is empty, the function returns 0.0.
*/

package main

import (
	"fmt"
	"math"
)

func MeanAbsoluteDeviation(numbers []float64) float64 {

	if len(numbers) == 0 {
		return 0.0
	}
	sum := 0.0
	for _, num := range numbers {
		sum += math.Abs(num)
	}
	mean := sum / float64(len(numbers))

	sum = 0.0
	for _, num := range numbers {
		sum += math.Abs(num - mean)
	}

	mad := sum / float64(len(numbers))
	return mad
}

func main() {
	numbers := []float64{1.0, 2.0, 3.0, 4.0}
	fmt.Println(MeanAbsoluteDeviation(numbers))
}

// >>> Output:
// 1
// 0.0
// 1
// 1.0
// 1
// 1.0
// 1
// 1.0
// 1
// 1.0
// 1
// 1.0
// 1