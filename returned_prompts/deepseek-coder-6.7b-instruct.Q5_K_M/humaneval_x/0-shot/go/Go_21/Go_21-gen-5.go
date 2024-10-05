
	min, max := mathutil.MinMax(numbers)
	rescaled := make([]float64, len(numbers))
	for i, num := range numbers {
		rescaled[i] = (num - min) / (max - min)
	}
	return rescaled
}

// MinMax returns the minimum and maximum values in the given slice.
func MinMax(numbers []float64) (float64, float64) {
	min := numbers[0]
	max := numbers[0]
	for _, num := range numbers {
		if num < min {
			min = num
		}
		if num > max {
			max = num
		}
	}
	return min, max
}

*/

package mathutil

import (
	"math"
)

// RescaleToUnit takes a slice of float64 numbers and returns another slice
// where the smallest number in the original slice becomes 0 and the largest becomes 1.
// The transformation is performed in-place, meaning that the original slice is modified.
func RescaleToUnit(numbers []float64) []float64 {
	min, max := minMax(numbers)
	for i, num := range numbers {
		numbers[i] = (num - min) / (max - min)
	}
	return numbers
}

// minMax returns the minimum and maximum values in the given slice.
func minMax(numbers []float64) (float64, float64) {
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
	return min, max
}

// Abs returns the absolute value of the input number.
func Abs(x float64) float64 {
	if x < 0 {
		return -x
	}
	return x
}

// Round rounds the input float64 to the nearest integer.
func Round(f float64) float64 {
	if f < 0