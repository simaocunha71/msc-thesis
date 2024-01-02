
// Given an array arr of integers, find the minimum number of elements that
// need to be changed to make the array palindromic. A palindromic array is an array that
// is read the same backwards and forwards. In one change, you can change one element to any other element.
// 
// For example:
// SmallestChange([1,2,3,5,4,7,9,6]) == 4
// SmallestChange([1, 2, 3, 4, 3, 2, 2]) == 1
// SmallestChange([1, 2, 3, 2, 1]) == 0
func SmallestChange(arr []int) int {
    if len(arr) < 2 {
        return 0
    }
    
	var s int = 0
	for _, v := range arr {
		s += 1
		if v == 0 || v > s {
			return s - 1
		}
		if v < s {
			return s
		}
	}
    return s
}