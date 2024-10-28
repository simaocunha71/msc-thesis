```go
package main

import (
    "fmt"
    "sort"
)

// Given an array of non-negative integers, return a copy of the given array after sorting,
// you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
// or sort it in descending order if the sum( first index value, last index value) is even.
// 
// Note:
// * don't change the given array.
// 
// Examples:
// * SortArray([]) => []
// * SortArray([5]) => [5]
// * SortArray([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
// * SortArray([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
func SortArray(array []int) []int {
    if len(array) == 0 {
        return array
    }
    sum := array[0] + array[len(array)-1]
    if sum%2 == 1 {
        sort.IntsAscending(array)
    } else {
        sort.IntsDescending(array)
    }
    return append([]int{}, array...)
}
```

This solution first calculates the sum of the first and last elements of the array. If the sum is odd, it sorts the array in ascending order using the `sort.IntsAscending` function. If the sum is even, it sorts the array in descending order using the `sort.IntsDescending` function. The `append` function is used to create a copy of the array. The original array is not modified. The function then returns the sorted array. If the input array is empty, the function returns the original array without modifying it.