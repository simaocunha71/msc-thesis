
// From a supplied list of numbers (of length at least two) select and return two that are the closest to each
// other and return them in order (smaller number, larger number).
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
// (2.0, 2.2)
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
// (2.0, 2.0)
func FindClosestElements(numbers []float64) [2]float64 {
	if len(numbers) < 2 {
		return numbers[0], numbers[len(numbers)-1]
	}

	var (
		min, max           float64
		previousMinMax    int32
		previousEven       bool
		even               int32
	)

	for i := 0; i < len(numbers); {
		number := numbers[i]
		// Emit even numbers at first.
		if previousEven == true && even > -1 {
			max = min + 1
		} else if even == -2 || number < max {
			even = -1
		} else {
			min = max - 1
		}
		i++
		if even > -1 {
			max += 1
		}
		previousMinMax = i
		previousEven = true
	}

	var (
		even, previousEven bool
		min, max           float64
	)

	for even = -2; even > -1 && i < len(numbers); {
		number := numbers[i]
		if even >= 0 || number <= min {
			even -= 1
		} else {
			even++
			max += 1
		}
		min = max - 1
		previousMinMax, previousEven = i, false