
// Return true is list elements are Monotonically increasing or decreasing.
// >>> Monotonic([1, 2, 4, 20])
// true
// >>> Monotonic([1, 20, 4, 10])
// false
// >>> Monotonic([4, 1, 0, -10])
// true
func Monotonic(l []int) bool {

	if len(l) == 1 {
		return true
	}

	for i := 1; i < len(l); i++ {
		if l[i] != l[i-1] {
			if l[i] > l[i-1] {
				for j := i + 1; j < len(l); j++ {
					if l[j] != l[j-1] && l[j] > l[j-1] {
						continue A
					}
					return false
				}
			} else {
				for j := i + 1; j < len(l); j++ {
					if l[j] != l[j-1] && l[j] < l[j-1] {
						continue A
					}
					return false
				}
			}
			return false
		}
	}
	return true
}
