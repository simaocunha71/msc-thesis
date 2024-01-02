
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
	if len(l) < 3 {
		return false
	}

	sums := make([]int, len(l))
	for i := 0; i < len(l); i++ {
		sums[i] = l[i] + sum(l[:i+1], sums)
	}

	return allDifferent(sums) && allSame(sums, 0)
}

// Returns a slice of sum values for the given list.
func sum(l []int, s []int) []int {
	r := make([]int, len(l))
	copy(r, l)
	sort.Ints(r)
	if i, j := 0, len(r)-1; r[i] < r[j] && r[j] != -1 {
		return s[:j+1] // remove first element
	} else if r[i] == r[j] && r[i] != -1 {
		return []int{0, 0} // add zeroes
	}
	return nil
}