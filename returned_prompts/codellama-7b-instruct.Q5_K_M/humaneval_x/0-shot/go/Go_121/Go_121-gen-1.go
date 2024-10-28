
// Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
// 
// Examples
// Solution([5, 8, 7, 1]) ==> 12
// Solution([3, 3, 3, 3, 3]) ==> 9
// Solution([30, 13, 24, 321]) ==>0
func Solution(lst []int) int {

	sum := 0
	for i:=0; i<len(lst); i++ {
		if (i%2) == 0 {
			if (lst[i] % 2) != 0 {
				sum += lst[i]
			}
		}
	}
	return sum
}
