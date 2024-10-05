
	for i, v := range operations {
		if i == 0 {
			if v < 0 {
				return true
			}
		} else {
			if v < 0 {
				return true
			}
			if operations[i-1]+v < 0 {
				return true
			}
		}
	}
	return false
}

// AboveZero([]int{1, 2, 3})
// false
// AboveZero([]int{1, 2, -4, 5})
// false
func AboveZero(operations []int) bool {

	for i, v := range operations {
		if i == 0 {
			if v > 0 {
				return true
			}
		} else {
			if v > 0 {
				return true
			}
			if operations[i-1]+v > 0 {
				return true
			}
		}
	}
	return false
}

// AboveZero([]int{1, 2, 3})
// true
// AboveZero([]int{1, 2, -4, 5})
// true
func AboveZero(operations []int) bool {

	for i, v := range operations {
		if i == 0 {
			if v > 0 {
				return true
			}
		} else {
			if v > 0 {
				return true
			}
			if operations[i-1]+v > 0 {
				return true
			}
		}
	}
	return false
}
