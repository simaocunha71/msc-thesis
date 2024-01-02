
// Return true is list elements are Monotonically increasing or decreasing.
// >>> Monotonic([1, 2, 4, 20])
// true
// >>> Monotonic([1, 20, 4, 10])
// false
// >>> Monotonic([4, 1, 0, -10])
// true
func Monotonic(l []int) bool {
	if len(l) == 0 {
		return true
	}

	min, max = l[0], l[len(l)-1]
	for i := range l {
		if min >= l[i+1] || max < l[i-1] {
			return false
		}
	}
	return true
}
