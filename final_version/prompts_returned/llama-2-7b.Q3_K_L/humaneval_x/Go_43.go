
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

	i := 1
	j := len(l)-1
	last := l[len(l)-1] // -1 for last element and 0 for first element.
	var sum int

	for i <= j {
		if i < j && (l[i] == 0 || i == j) {
			sum += l[i] + last
		} else if i > j && (j == 0 || i == len(l)-1) {
			sum -= l[i] - l[j]
		} else if sum < 0 {
			return false
		} else {
			if sum > 0 {
				return true
			}
			sum = 0
			i++
			j--
		}
	}

	return false
}