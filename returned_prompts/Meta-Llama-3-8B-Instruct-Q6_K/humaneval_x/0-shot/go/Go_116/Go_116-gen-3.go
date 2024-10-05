Here is the solution in Go:

```go
import (
    "fmt"
    "sort"
)

// In this Kata, you have to sort an array of non-negative integers according to
// number of ones in their binary representation in ascending order.
// For similar number of ones, sort based on decimal value.
// 
// It must be implemented like this:
// >>> SortArray([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
// >>> SortArray([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
// >>> SortArray([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
func SortArray(arr []int) []int {

    // Convert each number to binary and count the number of ones
    binCounts := make([]int, len(arr))
    for i, num := range arr {
        bin := fmt.Sprintf("%b", num)
        binCounts[i] = strings.Count(bin, "1")
    }

    // Sort the array based on the number of ones and the decimal value
    sort.Slice(arr, func(i, j int) bool {
        if binCounts[i] != binCounts[j] {
            return binCounts[i] < binCounts[j]
        }
        return arr[i] < arr[j]
    })

    return arr
}
```


This solution works by first counting the number of ones in the binary representation of each number in the array. Then it sorts the array based on these counts and the decimal values of the numbers. The sort.Slice function is used to sort the array. The sorting function is a lambda function that compares two elements of the array. If the number of ones in the binary representation of the two elements is different, it returns true if the first element has fewer ones. If the number of ones is the same, it returns true if the first element is smaller. The sort.Slice function uses this function to sort the array. Finally, the sorted array is returned.