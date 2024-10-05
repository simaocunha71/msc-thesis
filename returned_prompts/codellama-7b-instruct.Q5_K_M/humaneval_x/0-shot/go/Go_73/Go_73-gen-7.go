
// Given an array arr of integers, find the minimum number of elements that
// need to be changed to make the array palindromic. A palindromic array is an array that
// is read the same backwards and forwards. In one change, you can change one element to any other element.
// 
// For example:
// SmallestChange([1,2,3,5,4,7,9,6]) == 4
// SmallestChange([1, 2, 3, 4, 3, 2, 2]) == 1
// SmallestChange([1, 2, 3, 2, 1]) == 0
func SmallestChange(arr []int) int {

	n := len(arr)
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, n)
	}

	for i := 0; i < n; i++ {
		dp[i][i] = 0
	}

	for i := 0; i < n-1; i++ {
		if arr[i] == arr[i+1] {
			dp[i][i+1] = 0
		} else {
			dp[i][i+1] = 1
		}
	}

	for i := 1; i < n; i++ {
		for j := 0; j < n-i; j++ {
			dp[j][j+i] = min(dp[j+1][j+i], dp[j][j+i-1]+1)
		}
	}

	return dp[0][n-1]
}


