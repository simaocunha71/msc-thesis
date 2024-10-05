    sum := 0.0
    for _, num := range numbers {
        sum += math.Abs(num)
    }
    mean := sum / float64(len(numbers))

B:
    sumOfDifferences := 0.0
    for _, num := range numbers {
        sumOfDifferences += math.Abs(num - mean)
    }

C:
    mad := sumOfDifferences / float64(len(numbers))
    return mad
}

I've marked the three parts as A, B and C.
A is calculating the mean of the numbers.
B is calculating the sum of the absolute differences between each number and the mean.
C is calculating the Mean Absolute Deviation, which is the average of B.

A: Yes, this is correct.

B: Yes, this is correct as well.

C: Yes, this is correct.
*/

import (
	"math"
)

// MeanAbsoluteDeviation calculates Mean Absolute Deviation of a slice of float64 numbers
func MeanAbsoluteDeviation(numbers []float64) float64 {
	sum := 0.0
	for _, num := range numbers {
		sum += num
	}
	mean := sum / float64(len(numbers))

	sumOfDifferences := 0.0
	for _, num := range numbers {
		sumOfDifferences += math.Abs(num - mean)
	}

	mad := sumOfDifferences / float64(len(numbers))
	return mad
}
