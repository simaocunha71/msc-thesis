
// Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
// 
// Examples
// Solution([5, 8, 7, 1]) ==> 12
// Solution([3, 3, 3, 3, 3]) ==> 9
// Solution([30, 13, 24, 321]) ==>0
func Solution(lst []int) int {
	if len(lst) == 0 {
		return 0
	}
	res := 0

	for i := 0; i < len(lst); i = i+2 {
		switch lst[i] % 2 {
		case 1: // odd
			if lst[i+1] == 0 {
				res += lst[i]
			} else {
				// we have to skip current index (i+1), because it is even
				res += lst[i-2] // left 
				res += lst[i+2] // right
				// print("left: ", res)
			}
		case 0:
			if lst[i+1] == 0 {
				res = -1 * res
			} else {
				// we have to skip current index (i+1), because it is even
				res += lst[i-2] // left 
				res += lst[i+2] // right
				// print("left: ", res)
			}
		default:
			if lst[i+1] == 0 {
				res += lst[i]
			} else {
				// we have to skip current index (i+1), because it is even
				res += lst[i-2] // left 
				res += lst[i+2] // right
				// print("left: ", res)
			}
		}
	}

	return res
}