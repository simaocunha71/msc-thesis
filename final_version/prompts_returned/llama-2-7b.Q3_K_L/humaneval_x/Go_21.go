
// Given list of numbers (of at least two elements), apply a linear transform to that list,
// such that the smallest number will become 0 and the largest will become 1
// >>> RescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])
// [0.0, 0.25, 0.5, 0.75, 1.0]
func RescaleToUnit(numbers []float64) []float64 {
	if len(numbers) < 2 {
		return numbers
	}
	result := make([]float64, 0, len(numbers))
	for _, number := range numbers {
		if number <= 0 {
			number = 0.0
		} else if number >= 1 {
			number = 1.0
		}
		result = append(result, number)
	}
	return result
}