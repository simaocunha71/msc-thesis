
// Given an array arr of integers, find the minimum number of elements that
// need to be changed to make the array palindromic. A palindromic array is an array that
// is read the same backwards and forwards. In one change, you can change one element to any other element.
// 
// For example:
// SmallestChange([1,2,3,5,4,7,9,6]) == 4
// SmallestChange([1, 2, 3, 4, 3, 2, 2]) == 1
// SmallestChange([1, 2, 3, 2, 1]) == 0
func SmallestChange(arr []int) int {

	l := len(arr)
	if l == 0 {
		return 0
	}
	// if l == 1 {
	// 	return 0
	// }

	// 1. find the odd-count
	// 2. find the even-count
	// 3. find the middle element
	// 4. compare the odd-count and even-count
	// 5. find the middle element

	oddCount, evenCount := 0, 0
	// middleElement := 0
	middleIndex := 0
	for i, v := range arr {
		if i == l/2 {
			middleIndex = i
		}

		if v%2 == 0 {
			evenCount++
		} else {
			oddCount++
		}
	}

	if oddCount > evenCount {
		return oddCount - evenCount
	}
	return evenCount - oddCount
}
