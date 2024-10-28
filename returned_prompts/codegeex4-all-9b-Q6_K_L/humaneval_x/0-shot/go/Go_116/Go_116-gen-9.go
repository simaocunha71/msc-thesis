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

    sort.Slice(arr, func(i, j int) bool {
        countI := 0
        countJ := 0

        for _, v := range fmt.Sprintf("%b", arr[i]) {
            if v == '1' {
                countI++
            }
        }

        for _, v := range fmt.Sprintf("%b", arr[j]) {
            if v == '1' {
                countJ++
            }
        }

        if countI == countJ {
            return arr[i] < arr[j]
        }

        return countI < countJ
    })

    return arr
}
```
