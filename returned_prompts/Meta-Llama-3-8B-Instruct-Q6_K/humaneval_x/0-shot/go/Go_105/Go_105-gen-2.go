Here is the solution in Go:
```go
import (
    "sort"
)

func ByLength(arr []int) []string {
    var result []string
    var digitNames = [...]string{"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}

    // Filter out numbers outside the range 1-9
    filtered := make([]int, 0)
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            filtered = append(filtered, num)
        }
    }

    // Sort the filtered array
    sort.Ints(filtered)

    // Reverse the sorted array
    reverse(filtered)

    // Convert the reversed array to string names
    for _, num := range filtered {
        result = append(result, digitNames[num])
    }

    return result
}

func reverse(arr []int) {
    for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
        arr[i], arr[j] = arr[j], arr[i]
    }
}
```


Here's a breakdown of the solution:

1. First, we filter out numbers outside the range 1-9 by creating a new slice `filtered` and appending only the numbers within the range.
2. Next, we sort the filtered array using `sort.Ints`.
3. We then reverse the sorted array using a helper function `reverse`.
4. Finally, we iterate over the reversed array and convert each number to its corresponding string name using the `digitNames` array.

The `reverse` function is a simple implementation of the in-place reversal algorithm, which swaps elements at the beginning and end of the array and moves towards the middle.

The `ByLength` function returns the resulting array of string names. If the input array is empty, it returns an empty array. If the array contains any numbers outside the range 1-9, they are ignored.