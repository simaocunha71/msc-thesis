
// From a supplied list of numbers (of length at least two) select and return two that are the closest to each
// other and return them in order (smaller number, larger number).
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
// (2.0, 2.2)
// >>> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
// (2.0, 2.0)
func FindClosestElements(numbers []float64) [2]float64 {

	sort.Float64s(numbers)
	a := numbers[0]
	b := numbers[1]
	for i, n := range numbers[2:] {
		if n-b < a-n {
			a = n
		} else {
			b = n
		}
		if i == len(numbers)-2 {
			break
		}
	}
	return [2]float64{a, b}
}
