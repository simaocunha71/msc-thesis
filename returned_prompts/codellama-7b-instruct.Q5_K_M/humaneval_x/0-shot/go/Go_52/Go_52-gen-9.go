
// Return true if all numbers in the list l are below threshold t.
// >>> BelowThreshold([1, 2, 4, 10], 100)
// true
// >>> BelowThreshold([1, 20, 4, 10], 5)
// false
func BelowThreshold(l []int,t int) bool {

	for _, v := range l {
		if v > t {
			return false
		}
	}
	return true
}
