Here is the solution in Go:
```go
import (
    "sort"
    "strings"
)

func ByLength(arr []int) []string {
    // Filter out integers that are not between 1 and 9 inclusive
    filtered := make([]int, 0)
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            filtered = append(filtered, num)
        }
    }

    // Sort the filtered array
    sort.Ints(filtered)

    // Reverse the sorted array
    reversed := reverse(filtered)

    // Replace each digit by its corresponding name
    result := make([]string, 0)
    for _, num := range reversed {
        switch num {
        case 1:
            result = append(result, "One")
        case 2:
            result = append(result, "Two")
        case 3:
            result = append(result, "Three")
        case 4:
            result = append(result, "Four")
        case 5:
            result = append(result, "Five")
        case 6:
            result = append(result, "Six")
        case 7:
            result = append(result, "Seven")
        case 8:
            result = append(result, "Eight")
        case 9:
            result = append(result, "Nine")
        }
    }

    return result
}

// Reverse an array
func reverse(arr []int) []int {
    reversed := make([]int, len(arr))
    for i, num := range arr {
        reversed[len(arr)-1-i] = num
    }
    return reversed
}
```
This solution first filters out integers that are not between 1 and 9 inclusive, then sorts the filtered array, reverses the sorted array, and finally replaces each digit by its corresponding name. The `reverse` function is used to reverse the array. The `ByLength` function returns the resulting array of strings. If the input array is empty, the function returns an empty array. If the array has any strange numbers, they are ignored.