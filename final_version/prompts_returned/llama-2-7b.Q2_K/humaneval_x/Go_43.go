
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
	if len(l) < 2 {
		return false
	}
	prevInt := int(0)
	for i := range l {
		sum := i + prevInt
		if sum > 0 && sum != i+1 {
			prevInt = sum
			continue
		}
		return false
	}
	return true
}
