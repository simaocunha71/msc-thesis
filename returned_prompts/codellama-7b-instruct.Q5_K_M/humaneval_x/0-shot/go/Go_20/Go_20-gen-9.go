
// From a supplied list of numbers (of length at least two) select and return two that are the closest to each
// other and return them in order (smaller number, larger number).
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
// (2.0, 2.2)
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
// (2.0, 2.0)
func FindClosestElements(numbers []float64) [2]float64 {

	// sort numbers
	sort.Float64s(numbers)

	// find the smallest difference
	var smallestDifference float64 = math.MaxFloat64
	var smallestDifferenceIndex int

	for i := 1; i < len(numbers); i++ {

		if numbers[i] - numbers[i-1] < smallestDifference {
			smallestDifference = numbers[i] - numbers[i-1]
			smallestDifferenceIndex = i
		}
	}

	// return the smallest difference
	return [2]float64{
		numbers[smallestDifferenceIndex-1],
		numbers[smallestDifferenceIndex],
	}
}

// From a supplied list of numbers (of length at least two) select and return two that are the closest to each
// other and return them in order (smaller number, larger number).
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
// (2.0, 2.2)
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
// (2.0, 2.0)
func FindClosestElements(numbers []float64) [2]float64 {

	// sort numbers
	sort.Float64s