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
    // 将数组转换为逆堆状态，依次对每项进行排序，以保证当前最大元素不会被下沉到最后一位
    reverse(arr)
    
    sortedArr := make([]int, 0, k+1)

    for i := range arr {
        if i == len(sortedArr)-1 || sort.SearchInts(arr[i:], sortedArr[len(sortedArr)]) >= 0 {
            sortedArr = append(sortedArr, arr[i])
        } else {
            sortedArr = append(sortedArr, arr[i])
        }
    }
    
    return sortedArr[:k+1]
}

func reverse(arr []int)  {
    n := len(arr) - 1
    for i := range arr {
        j:=i
        for ;j < n; j++ {
            if sort.SearchInts(arr, arr[j]) >= 0 {
