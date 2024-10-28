
// PairsSumToZero takes a list of integers as an input.
// it returns true if there are two distinct elements in the list that
// sum to zero, and false otherwise.
// >>> PairsSumToZero([1, 3, 5, 0])
// false
// >>> PairsSumToZero([1, 3, -2, 1])
// false
// >>> PairsSumToZero([1, 2, 3, 7])
// false
// >>> PairsSumToZero([2, 4, -5, 3, 5, 7])
// true
// >>> PairsSumToZero([1])
// false
func PairsSumToZero(l []int) bool {

	// first we make a map of the list,
	// we use the map to count the number of elements in the list
	// and also to find the number of elements that sum to zero

	m := make(map[int]int)
	for _, v := range l {
		m[v]++
	}

	// now we look for the number of elements that sum to zero

	for _, v := range l {
		if m[v] > 1 {
			return true
		}
	}

	return false
}
