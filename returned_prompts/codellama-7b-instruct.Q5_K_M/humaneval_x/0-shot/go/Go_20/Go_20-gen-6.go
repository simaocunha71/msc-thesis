
// From a supplied list of numbers (of length at least two) select and return two that are the closest to each
// other and return them in order (smallest number, largest number).
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
// (2.0, 2.2)
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
// (2.0, 2.0)
func FindClosestElements(numbers []float64) [2]float64 {

	// Sort the list in ascending order
	sort.Float64s(numbers)

	// Find the index of the closest pair of numbers
	index := 0
	for i := 0; i < len(numbers)-1; i++ {
		if math.Abs(numbers[i]-numbers[i+1]) < math.Abs(numbers[index]-numbers[index+1]) {
			index = i
		}
	}

	// Return the closest pair of numbers
	return [2]float64{numbers[index], numbers[index+1]}
}
