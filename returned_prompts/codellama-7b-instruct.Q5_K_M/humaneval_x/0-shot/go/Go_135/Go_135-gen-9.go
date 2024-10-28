
// Create a function which returns the largest index of an element which
// is not greater than or equal to the element immediately following it. If
// no such element exists then return -1. The given array will not contain
// duplicate values.
// 
// Examples:
// CanArrange([1,2,4,3,5]) = 3
// CanArrange([1,2,3]) = -1
func CanArrange(arr []int) int {

	for i := 0; i < len(arr)-1; i++ {
		if arr[i] >= arr[i+1] {
			return i
		}
	}
	return -1
}
