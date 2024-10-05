
// Given list of numbers (of at least two elements), apply a linear transform to that list,
// such that the smallest number will become 0 and the largest will become 1
// >>> RescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])
// [0.0, 0.25, 0.5, 0.75, 1.0]
func RescaleToUnit(numbers []float64) []float64 {

	// Find the smallest and largest values.
	smallest := numbers[0]
	largest := numbers[0]
	for _, num := range numbers {
		if num < smallest {
			smallest = num
		}
		if num > largest {
			largest = num
		}
	}

	// Calculate the scale factor.
	scale := 1.0 / (largest - smallest)

	// Rescale the numbers.
	rescaled := make([]float64, len(numbers))
	for i, num := range numbers {
		rescaled[i] = (num - smallest) * scale
	}

	return rescaled
}
