
// Given a positive integer n, you have to make a pile of n levels of stones.
// The first level has n stones.
// The number of stones in the next level is:
// - the next odd number if n is odd.
// - the next even number if n is even.
// Return the number of stones in each level in a list, where element at index
// i represents the number of stones in the level (i+1).
// 
// Examples:
// >>> MakeAPile(3)
// [3, 5, 7]
func MakeAPile(n int) []int {

	// create list to store the result
	result := make([]int, n)

	// set the first level
	result[0] = n

	// iterate over the levels
	for i := 1; i < n; i++ {
		// get the next number to be used
		next := nextNumber(result[i-1])

		// add to the next level
		result[i] = next
	}

	// return the result
	return result
}

// get the next number
func nextNumber(n int) int {
	if n%2 == 0 {
		return n + 1
	}
	return n + 2
}
