
// You are given a non-empty list of positive integers. Return the greatest integer that is greater than zero, and has a frequency greater than or equal to the value of the integer itself.
// The frequency of an integer is the number of times it appears in the list.
// If no such a value exist, return -1.
// Examples:
// Search([4, 1, 2, 2, 3, 1]) == 2
// Search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
// Search([5, 5, 4, 4, 4]) == -1
func Search(lst []int) int {

	// create a map of frequency of each integer
	frequency := make(map[int]int)
	for _, v := range lst {
		frequency[v]++
	}
	// find the max frequency
	var maxFreq int
	for _, v := range frequency {
		if v > maxFreq {
			maxFreq = v
		}
	}
	// find the value with max frequency
	for k, v := range frequency {
		if v == maxFreq {
			return k
		}
	}
	return -1
}
