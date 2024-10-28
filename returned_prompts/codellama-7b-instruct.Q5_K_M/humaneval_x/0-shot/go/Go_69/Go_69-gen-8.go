
// You are given a non-empty list of positive integers. Return the greatest integer that is greater than zero, and has a frequency greater than or equal to the value of the integer itself.
// The frequency of an integer is the number of times it appears in the list.
// If no such a value exist, return -1.
// Examples:
// Search([4, 1, 2, 2, 3, 1]) == 2
// Search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
// Search([5, 5, 4, 4, 4]) == -1
func Search(lst []int) int {

	// Write your code here
	m := map[int]int{}
	for _, v := range lst {
		if v > 0 {
			m[v]++
		}
	}
	var maxValue int
	for k, v := range m {
		if k >= v && k > maxValue {
			maxValue = k
		}
	}
	if maxValue > 0 {
		return maxValue
	} else {
		return -1
	}
}
