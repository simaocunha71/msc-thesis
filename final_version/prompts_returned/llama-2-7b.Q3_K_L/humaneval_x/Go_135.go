
// Create a function which returns the largest index of an element which
// is not greater than or equal to the element immediately preceding it. If
// no such element exists then return -1. The given array will not contain
// duplicate values.
// 
// Examples:
// CanArrange([1,2,4,3,5]) = 3
// CanArrange([1,2,3]) = -1
func CanArrange(arr []int) int {
	if len(arr) == 0 {
		return -1
	}

	// we will loop from left to right and compare the current node with its next
	last := 0
	curr := 1
	for curr < len(arr) {
		// if the element is smaller than last
		if arr[curr] <= arr[last+1] {
			// change it to -1
			return -1
		} else {
			// else compare and store for future use
			last = curr
		}
		curr++
	}
	if last == 0 {
		return -1
	} else {
		return last + 1
	}
}
