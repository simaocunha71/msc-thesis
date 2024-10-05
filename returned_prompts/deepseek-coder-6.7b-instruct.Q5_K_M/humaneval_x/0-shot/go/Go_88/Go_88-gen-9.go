    // Create a copy of the array
    copyArray := make([]int, len(array))
    copy(copyArray, array)

    // sort the copyArray
    sort.Ints(copyArray)

    // check if the sum of the first and last index value is odd or even
    if (copyArray[0] + copyArray[len(copyArray)-1]) % 2 == 0 {
        // if even, reverse the copyArray
        for i := 0; i < len(copyArray)/2; i++ {
            copyArray[i], copyArray[len(copyArray)-1-i] = copyArray[len(copyArray)-1-i], copyArray[i]
        }
    }
    return copyArray
}
```

## Answer:
```go
import  (
    "sort"
)

// Given an array of non-negative integers, return a copy of the given array after sorting,
// you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
// or sort it in descending order if the sum( first index value, last index value) is even.
// 
// Note:
//  don't change the given array.
// 
// Examples:
//  SortArray([]) => []
//  SortArray([5]) => [5]
//  SortArray([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
//  SortArray([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
func SortArray(array  []int)  []int  {

    // Create a copy of the array
    copyArray := make([]int, len(array))
    copy(copyArray, array)

    // sort the copyArray
    sort.Ints(copyArray)

    // check if the sum of the first and last index value is odd or even
    if (copyArray[0] + copyArray[len(copyArray)-