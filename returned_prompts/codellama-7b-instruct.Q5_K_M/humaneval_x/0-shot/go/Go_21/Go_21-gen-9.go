
// Given list of numbers (of at least two elements), apply a linear transform to that list,
// such that the smallest number will become 0 and the largest will become 1
// >>> RescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])
// [0.0, 0.25, 0.5, 0.75, 1.0]
func RescaleToUnit(numbers []float64) []float64 {
	// Find the smallest and largest element in the list
	smallest := math.Inf(1)
	largest := math.Inf(-1)
	for _, number := range numbers {
		if number < smallest {
			smallest = number
		}
		if number > largest {
			largest = number
		}
	}

	// Rescale the list to unit range
	result := make([]float64, len(numbers))
	for i, number := range numbers {
		result[i] = (number - smallest) / (largest - smallest)
	}
	return result
}
