
// From a supplied list of numbers (of length at least two) select and return two that are the closest to each
// other and return them in order (smaller number, larger number).
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
// (2.0, 2.2)
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
// (2.0, 2.0)
func FindClosestElements(numbers []float64) [2]float64 {
	if len(numbers) < 2 {
		panic("at least two numbers are required")
	}
	var (
		minDiff = math.MaxFloat64
		a, b    float64
	)
	for i := range numbers {
		for j := range numbers {
			if i == j {
				continue
			}
			diff := math.Abs(numbers[i] - numbers[j])
			if diff < minDiff {
				minDiff = diff
				a, b = numbers[i], numbers[j]
			}
		}
	}
	return [2]float64{a, b}
}
