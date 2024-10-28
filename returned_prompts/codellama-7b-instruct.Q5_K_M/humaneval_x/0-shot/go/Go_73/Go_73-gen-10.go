
// Given an array arr of integers, find the minimum number of elements that need to be changed to make the array palindromic. A palindromic array is an array that is read the same backwards and forwards. In one change, you can change one element to any other element.
// 
// For example:
// SmallestChange([1,2,3,5,4,7,9,6]) == 4
// SmallestChange([1, 2, 3, 4, 3, 2, 2]) == 1
// SmallestChange([1, 2, 3, 2, 1]) == 0
func SmallestChange(arr []int) int {

	// 1. check if the array is palindromic
	// 2. check if the array is single element palindromic
	// 3. check if the array is double element palindromic
	// 4. check if the array is multiple elements palindromic
	// 5. return the minimum value

	// 1. check if the array is palindromic
	for i := 0; i < len(arr); i++ {
		if arr[i] != arr[len(arr)-1-i] {
			return -1
		}
	}

	// 2. check if the array is single element palindromic
	if len(arr) == 1 {
		return 0
	}

	// 3. check if the array is double element palindromic
	if len(arr) == 2 {
		if arr[0] != arr[1] {
			return 1
		}
		return 0
	}

	// 4. check if the array is multiple elements palindromic
	// 5. return the minimum value
	return -1
}
