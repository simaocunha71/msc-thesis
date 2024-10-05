
// Create a function which returns the largest index of an element which
// is not greater than or equal to the element immediately preceding it. If
// no such element exists then return -1. The given array will not contain
// duplicate values.
// 
// Examples:
// CanArrange([1,2,4,3,5]) = 3
// CanArrange([1,2,3]) = -1
func CanArrange(arr []int) int {

	// Check for a valid input
	if len(arr) < 2 {
		return -1
	}

	// Get the length of the array
	l := len(arr)

	// Iterate over the array
	for i := 0; i < l; i++ {

		// Check the next element
		if i+1 < l && arr[i] >= arr[i+1] {
			continue
		}

		// Check the previous element
		if i-1 >= 0 && arr[i-1] >= arr[i] {
			continue
		}

		// We have a match
		return i
	}

	// No match was found
	return -1
}

