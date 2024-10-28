func PairsSumToZero(l []int) bool {
	for i, a := range l {
		for j, b := range l {
			if i != j && a+b == 0 {
				return true
			}
		}
	}
	return false
}
Comments:

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
	for i, a := range l {
		for j, b := range l {
			if i != j && a+b == 0 {
				return true
			}
		}
	}
	return false
}