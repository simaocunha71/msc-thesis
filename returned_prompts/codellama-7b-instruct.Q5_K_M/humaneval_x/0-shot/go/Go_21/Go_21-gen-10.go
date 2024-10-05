
// Given list of numbers, apply a linear transform to that list,
// such that the smallest number will become 0 and the largest will become 1
// >>> RescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])
// [0.0, 0.25, 0.5, 0.75, 1.0]
func RescaleToUnit(numbers []float64) []float64 {

	// Find the smallest and largest numbers in the list
	min, max := numbers[0], numbers[0]
	for _, n := range numbers {
		if n < min {
			min = n
		}
		if n > max {
			max = n
		}
	}

	// Calculate the range of values (difference between min and max)
	rangeOfValues := max - min

	// Create a new list with the same length as the input
	rescaledNumbers := make([]float64, len(numbers))

	// For each number in the list, calculate the rescaled value
	// and store it in the new list
	for i, n := range numbers {
		rescaledNumbers[i] = (n - min) / rangeOfValues
	}

	return rescaledNumbers
}
