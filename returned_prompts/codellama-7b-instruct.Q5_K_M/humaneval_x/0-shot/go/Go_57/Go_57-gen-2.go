
// Return true is list elements are Monotonically increasing or decreasing.
// >>> Monotonic([1, 2, 4, 20])
// true
// >>> Monotonic([1, 20, 4, 10])
// false
// >>> Monotonic([4, 1, 0, -10])
// true
func Monotonic(l []int) bool {

	// if list has only one element then it is monotonic
	if len(l) == 1 {
		return true
	}

	// if list has two elements then it is monotonic
	if len(l) == 2 {
		return true
	}

	// if list elements are not monotonic then return false
	for i := 1; i < len(l); i++ {
		if l[i] != l[i-1] {
			return false
		}
	}

	// if list elements are monotonic then return true
	return true
}
