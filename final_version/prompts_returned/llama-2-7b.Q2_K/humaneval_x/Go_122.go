import (
    "strconv"
)

// Given a non-empty array of integers arr and an integer k, return
// the sum of the elements with at most two digits from the first k elements of arr.
// 
// Example:
// 
// Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
// Output: 24 # sum of 21 + 3
// 
// Constraints:
// 1. 1 <= len(arr) <= 100
// 2. 1 <= k <= len(arr)
func AddElements(arr []int, k int) int {
    if len(arr) == 0 || k >= len(arr) {
        return -1 // out of range
    }
    
    temp := arr[k+1:]
    sumOfTail := 0
    for i := 0; i < len(temp); i++ {
        if strconv.Itoa(temp[i]) >= "9" && strconv.Itoa(temp[i-1]) <= "2", strconv.Itoa(temp[i-1]) + strconv.Itoa(temp[i]) >= "03" {
            sumOfTail += strconv.Atoi(strconv.Itoa(temp[i]))
        } else {
            break
        }
    }
    
    // return 12 + 14 = 26
    // return strconv.Itoa(arr[k]) + sumOfTail
    return AddElements(arr[:k+1], k+1) + temp[0]
}