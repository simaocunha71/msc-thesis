
// Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
// 
// Examples
// Solution([5, 8, 7, 1]) ==> 12
// Solution([3, 3, 3, 3, 3]) ==> 9
// Solution([30, 13, 24, 321]) ==>0
func Solution(lst []int) int {
	var s int = 0
	for i := 1; i <= len(lst); i++ {
		if lst[i] % 2 == 1 && (i < len(lst)) && (lst[len(lst)-1]%2==1){
			s += lst[i]
		}
	}
	return s
}
