
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
	var piles []int
	for i := 0; i < n; i++ {
		piles = append(piles, n)
		n = n + 1
		if n%2 == 0 {
			n += 1
		}
	}
	return piles
}
