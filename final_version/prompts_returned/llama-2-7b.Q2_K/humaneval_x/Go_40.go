
// TriplesSumToZero takes a list of integers as an input.
// it returns true if there are three distinct elements in the list that
// sum to zero, and false otherwise.
// 
// >>> TriplesSumToZero([1, 3, 5, 0])
// false
// >>> TriplesSumToZero([1, 3, -2, 1])
// true
// >>> TriplesSumToZero([1, 2, 3, 7])
// false
// >>> TriplesSumToZero([2, 4, -5, 3, 9, 7])
// true
// >>> TriplesSumToZero([1])
// false
func TriplesSumToZero(l []int) bool {
	if len(l) == 0 {
		return false
	} else if len(l) < 3 { // the length of l must be at least three.
		return true
	} else if len(l)%3 != 0 { // we want exactly three elements in l, so that's not allowed.
		return false
	} else { // everything went well so far -> we can check the sum of each triplet.
		sum0 := (len(l)) / 3 + len(l)%3*2/3
		for i, j := range l {
			if i == j {
				continue
			} else if i+j != -1 && i-j != -1 && sum0 > 0 { // we have a triplet of three consecutive numbers. This is valid as long as their sum is greater than zero.
				return true
			}
		}
	}
	return false
}
