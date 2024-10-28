Here is a possible solution in Go:
```go
import (
    "fmt"
    "sort"
)

type pair struct {
    val int
    ones int
}

func SortArray(arr []int) []int {
    pairs := make([]pair, len(arr))
    for i, v := range arr {
        pairs[i].val = v
        pairs[i].ones = binCount(v)
    }
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].ones == pairs[j].ones {
            return pairs[i].val < pairs[j].val
        }
        return pairs[i].ones < pairs[j].ones
    })
    result := make([]int, len(arr))
    for i, p := range pairs {
        result[i] = p.val
    }
    return result
}

func binCount(n int) int {
    count := 0
    for n > 0 {
        n &= n - 1
        count++
    }
    return count
}
```
Here's an explanation of the solution:

1. We define a `pair` struct to store the original value and the count of ones in the binary representation of each number.
2. We create a slice of `pair` structs and fill it with the original values and the count of ones for each number using the `binCount` function.
3. We use the `sort.Slice` function to sort the slice of `pair` structs based on the count of ones and then the decimal value.
4. We create a new slice to store the sorted values and fill it with the original values from the sorted `pair` slice.
5. We return the sorted slice.

The `binCount` function counts the number of ones in the binary representation of a given number by repeatedly subtracting 1 from the number and counting the number of times this operation can be performed.

Note that this solution has a time complexity of O(n log n) due to the sorting, where n is the length of the input array. The `binCount` function has a time complexity of O(log n) and is called n times, so the total time complexity is dominated by the sorting. The space complexity is O(n) for the slice of `pair` structs.