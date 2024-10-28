
// Return true if list elements are Monotonically increasing or decreasing.
// >>> Monotonic([1, 2, 4, 20])
// true
// >>> Monotonic([1, 20, 4, 10])
// false
// >>> Monotonic([4, 1, 0, -10])
// true
func Monotonic(l []int) bool {
	if len(l) < 2 {
		return true
	}
	for i := 1; i < len(l); i++ {
		if l[i] < l[i-1] {
			return false
		}
	}
	return true
}

// Return true if list elements are Monotonically increasing or decreasing.
// >>> Monotonic([1, 2, 4, 20])
// true
// >>> Monotonic([1, 20, 4, 10])
// false
// >>> Monotonic([4, 1, 0, -10])
// true
func Monotonic(l []int) bool {
	if len(l) < 2 {
		return true
	}
	for i := 1; i < len(l); i++ {
		if l[i] < l[i-1] {
			return false
		}
	}
	return true
}
