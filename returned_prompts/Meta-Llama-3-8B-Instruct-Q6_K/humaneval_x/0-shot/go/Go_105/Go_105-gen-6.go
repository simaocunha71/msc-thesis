Here is a solution in Go that satisfies the problem requirements:

```go
import (
    "sort"
    "strings"
)

func ByLength(arr []int) []string {
    // Filter out numbers not in the range 1-9
    filtered := make([]int, 0)
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            filtered = append(filtered, num)
        }
    }

    // Sort the filtered array
    sort.Ints(filtered)

    // Reverse the sorted array
    reversed := make([]int, len(filtered))
    copy(reversed, filtered)
    for i := 0; i < len(reversed); i++ {
        reversed[i] = filtered[len(filtered)-1-i]
    }

    // Convert the reversed array to strings
    names := make([]string, 0)
    for _, num := range reversed {
        switch num {
        case 1:
            names = append(names, "One")
        case 2:
            names = append(names, "Two")
        case 3:
            names = append(names, "Three")
        case 4:
            names = append(names, "Four")
        case 5:
            names = append(names, "Five")
        case 6:
            names = append(names, "Six")
        case 7:
            names = append(names, "Seven")
        case 8:
            names = append(names, "Eight")
        case 9:
            names = append(names, "Nine")
        }
    }

    return names
}

func main() {
    arr := []int{2, 1, 1, 4, 5, 8, 2, 3}
    result := ByLength(arr)
    fmt.Println(result) // Output: ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
}
```

This solution works by first filtering out numbers not in the range 1-9, then sorting the remaining numbers, reversing the sorted array, and finally converting the reversed array to strings using a switch statement. The result is an array of strings, where each string is the name of a number from 1 to 9. If the input array is empty, the function returns an empty array. If the array contains any numbers outside the range 1-9, the function will ignore those numbers and return an array containing the names of the numbers in the range