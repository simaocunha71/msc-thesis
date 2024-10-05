The problem can be solved by sorting the array and then checking if the sorted array is equal to the original array. 

Here is the solution in Go:

```go
import (
    "math"
    "sort"
)

func MoveOneBall(arr []int) bool {
    if len(arr) == 0 {
        return true
    }
    sort.Ints(arr)
    for i := 0; i < len(arr)-1; i++ {
        if arr[i] > arr[i+1] {
            return false
        }
    }
    return true
}
```

In this solution, we first check if the array is empty. If it is, we return true because an empty array is considered sorted. Then we sort the array using the sort.Ints function from the sort package. After sorting, we iterate through the array and check if any element is greater than the next one. If we find such an element, we return false because it is not possible to get a non-decreasing order by performing right shift operations. If we don't find any such element, we return true because the array is already sorted. 

This solution has a time complexity of O(n log n) due to the sorting operation, where n is the length of the array. The space complexity is O(1) because we only use a constant amount of space to store the array and the result. 

Note that this solution assumes that the array contains unique elements, as stated in the problem description. If the array can contain duplicate elements, we need to modify the solution accordingly. 

Also, this solution does not consider the number of right shift operations needed to get the sorted array. If we need to consider this, we would need to use a different approach. 

For example, we could use a greedy algorithm to find the minimum number of right shift operations needed to get the sorted array. This would involve iterating through the array and finding the maximum element that is less than the current element. We would then subtract this maximum element from the current element to get the minimum number of right shift operations needed to make the current element the maximum. We would repeat this process until we have iterated through the entire array. 

This approach would have a time complexity of O(n) and a space complexity of O(1), where n is the length of the array. However, it would not work correctly if the array contains duplicate elements. 

In summary, the solution provided is a simple and efficient way to determine if it is possible to get