
// From a supplied list of numbers (of length at least two) select and return two that are the closest to each
// other and return them in order (smaller number, larger number).
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
// (2.0, 2.2)
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
// (2.0, 2.0)
func FindClosestElements(numbers []float64) [2]float64 {
	var minDiff float64 = math.MaxFloat64
	var closestPair [2]float64
	for i := 0; i < len(numbers)-1; i++ {
		for j := i + 1; j < len(numbers); j++ {
			if math.Abs(numbers[j]-numbers[i]) < minDiff {
				minDiff = math.Abs(numbers[j] - numbers[i])
				closestPair[0] = numbers[i]
				closestPair[1] = numbers[j]
			}
		}
	}
	return closestPair
}

