import (
    "sort"
)

// Given an array arr of integers and a positive integer k, return a sorted list
// of length k with the Maximum k numbers in arr.
// 
// Example 1:
// 
// Input: arr = [-3, -4, 5], k = 3
// Output: [-4, -3, 5]
// 
// Example 2:
// 
// Input: arr = [4, -4, 4], k = 2
// Output: [4, 4]
// 
// Example 3:
// 
// Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
// Output: [2]
// 
// Note:
// 1. The length of the array will be in the range of [1, 1000].
// 2. The elements in the array will be in the range of [-1000, 1000].
// 3. 0 <= k <= len(arr)
func Maximum(arr []int, k int) []int {
    sort.Ints(arr)
    
    return arr[sort.SearchLen(len(arr), func(i int) bool {
        return arr[i] > k
    })] // 입력은 정렬되어 오기 때문에 아무리 거꾸로 sort 하고 조금만 arr의 크기를 넣을수 없어도 된다.
}