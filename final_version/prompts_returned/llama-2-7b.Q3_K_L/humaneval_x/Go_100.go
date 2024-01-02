
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
	if n%2 == 0 {
		return make([]int, 1)
	} else {
		var level int = 1
		for i := 1; ; i++ {
			level *= 2
			if i > level {
				break
			}
		}
		return make([]int, level)
	}
}