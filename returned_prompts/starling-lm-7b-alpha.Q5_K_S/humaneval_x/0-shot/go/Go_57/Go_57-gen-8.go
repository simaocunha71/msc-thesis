
	if len(l) == 0 {
		return true
	}

	mono := true
	for i := 1; i < len(l); i++ {
		if l[i] < l[i-1] {
			mono = false
		}
	}

	return mono
}







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

	mono := true
	for i := 1; i < len(l); i++ {
		if l[i] < l[i-1] {
			mono = false
		}
	}

	return mono
}









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

	mono := true
	for i := 1; i < len(l); i++ {
		if l[i] < l[i-1] {
			mono = false
		}
	}

	return mono
}

























































