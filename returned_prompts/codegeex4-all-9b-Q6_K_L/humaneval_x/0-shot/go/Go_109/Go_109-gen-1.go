import (
    "math"
    "sort"
)

// We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
// numbers in the array will be randomly ordered. Your task is to determine if
// it is possible to get an array sorted in non-decreasing order by performing
// the following operation on the given array:
// You are allowed to perform right shift operation any number of times.
// 
// One right shift operation means shifting all elements of the array by one
// position in the right direction. The last element of the array will be moved to
// the starting position in the array i.e. 0th index.
// 
// If it is possible to obtain the sorted array by performing the above operation
// then return true else return false.
// If the given array is empty then return true.
// 
// Note: The given list is guaranteed to have unique elements.
// 
// For Example:
// 
// MoveOneBall([3, 4, 5, 1, 2])==>true
// Explanation: By performin 2 right shift operations, non-decreasing order can
// be achieved for the given array.
// MoveOneBall([3, 5, 4, 1, 2])==>false
// Explanation:It is not possible to get non-decreasing order for the given
// array by performing any number of right shift operations.
func MoveOneBall(arr []int) bool {

    if len(arr) == 0 {
        return true
    }

    sortedArr := make([]int, len(arr))
    copy(sortedArr, arr)
    sort.Ints(sortedArr)

    shiftCount := 0
    for i := 0; i < len(arr); i++ {
        if arr[i] == sortedArr[shiftCount] {
            shiftCount++
        } else {
            shiftCount = 0
        }
    }

    return shiftCount == len(arr)
}

// Test cases
func TestMoveOneBall(t *testing.T) {
    t.Run("Test case 1", func(t *testing.T) {
        arr := []int{3, 4, 5, 1, 2}
        expected := true
        result := MoveOneBall(arr)
        if result != expected {
            t.Errorf("Expected %v, but got %v", expected, result)
        }
    })

    t.Run("Test case 