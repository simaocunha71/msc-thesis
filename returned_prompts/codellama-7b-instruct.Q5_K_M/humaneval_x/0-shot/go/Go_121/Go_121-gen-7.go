
// Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
// 
// Examples
// Solution([5, 8, 7, 1]) ==> 12
// Solution([3, 3, 3, 3, 3]) ==> 9
// Solution([30, 13, 24, 321]) ==>0
func Solution(lst []int) int {

	// write your code in Go 1.4
	var res int
	for i := 0; i < len(lst); i += 2 {
		if i%2 == 0 {
			if lst[i]%2 != 0 {
				res += lst[i]
			}
		}
	}
	return res
}
