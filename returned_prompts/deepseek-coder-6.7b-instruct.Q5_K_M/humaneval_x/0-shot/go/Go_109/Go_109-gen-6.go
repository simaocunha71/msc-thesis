    for i := range arr {
        for j := 0; j < len(arr)-1; j++ {
            if arr[j] > arr[j+1] {
                arr[j], arr[j+1] = arr[j+1], arr[j]
            }
        }
        if isSorted(arr) {
            return true
        }
        arr = append([]int{arr[len(arr)-1]}, arr[:len(arr)-1]...)
    }
    return false
}

func isSorted(arr []int) bool {
    for i := 0; i < len(arr)-1; i++ {
        if arr[i] > arr[i+1] {
            return false
        }
    }
    return true
}

In the above code, the function isSorted checks if the array is sorted in non-decreasing order. The function MoveOneBall checks if it's possible to obtain a sorted array by performing a right shift operation any number of times.

The main loop in MoveOneBall shifts the last element to the first position and checks if the array is sorted. If it is, the function returns true. If it isn't, the function continues to the next iteration.

If the function has gone through all possible shift combinations without finding a sorted array, it returns false.

One thing to note is that this code could be optimized. The current solution has a time complexity of O(n^2) due to the nested loop in the MoveOneBall function. A more efficient solution could be to first determine the index of the first element in the sorted array. Then, the array is shifted to bring this element to the front. After that, the array is checked if it's sorted. This solution would have a time complexity of O(n).
*/

import (
	"fmt"
)

func main() {
	fmt.Println(MoveOneBall([]int{3, 4, 5, 1, 2})) // true
	fmt.Println(MoveOneBall([]int{3, 5, 4, 1, 2})) // false
	fmt.Println(MoveOneBall([]int{}))               // true