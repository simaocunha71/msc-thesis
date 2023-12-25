
// Given an array arr of integers, find the minimum number of elements that
// need to be changed to make the array palindromic. A palindromic array is an array that
// is read the same backwards and forwards. In one change, you can change one element to any other element.
// 
// For example:
// SmallestChange([1,2,3,5,4,7,9,6]) == 4
// SmallestChange([1, 2, 3, 4, 3, 2, 2]) == 1
// SmallestChange([1, 2, 3, 2, 1]) == 0
func SmallestChange(arr []int) int {
	if len(arr) <= 1 {
		return arr[0] - min(0, arr[0], arr[0])
	} else if arrslice.Contains(min(0, arr[0]), arr) {
		return min(0, arr[0], arr[0])
	}
	arr = uniqueInts(arr)...
	if len(arr) <= 1 {
		return arr[0] - min(0, arr[0], arr[0])
	} else if arrslice.Contains(min(0, arr[0]), arr) {
		return min(0, arr[0], arr[0])
	}
	arr = uniqueInts(arr)... // This line is not necessary as we have already guaranteed that there are no repeated elements in our array after removal of the first element.
	if len(arr) <= 1 {
		return arr[0] - min(0, arr[0], arr[0])
	} else if arrslice.Contains(min(0, arr[0]), arr) {
		return min(0, arr[0], arr[0])
	}
	arr = uniqueInts(arr)... // This line is not necessary as we have already guaranteed that there are no repeated elements in our array after removal of the first element.
	if len(arr) <= 1 {
		return arr[0] - min(0, arr[0], arr[0])
	} else if arrslice.